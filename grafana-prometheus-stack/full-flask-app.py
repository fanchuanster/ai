from flask import Flask, request
import logging
import structlog
from prometheus_client import start_http_server, Counter, Histogram
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# ========== Structured Logging ==========
logging.basicConfig(format="%(message)s", level=logging.INFO)
structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.INFO))
logger = structlog.get_logger()

# ========== Tracing Setup ==========
resource = Resource(attributes={
    SERVICE_NAME: "flask-observability-app"
})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True))
trace.get_tracer_provider().add_span_processor(span_processor)

# ========== Flask App ==========
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# ========== Metrics ==========
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency', ['endpoint'])

# ========== Routes ==========
@app.route("/")
def hello():
    with REQUEST_LATENCY.labels(endpoint="/").time():
        REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
        logger.info("hello_world_called", user_ip=request.remote_addr)

        with tracer.start_as_current_span("handle_hello_request") as span:
            span.set_attribute("http.method", "GET")
            span.set_attribute("user.ip", request.remote_addr)
            return "Hello, world! 👋"

@app.route("/fail")
def fail():
    with tracer.start_as_current_span("simulate_failure") as span:
        span.set_attribute("http.method", "GET")
        try:
            raise ValueError("Simulated error for observability demo")
        except Exception as e:
            logger.error("error_occurred", error=str(e))
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            return "Internal Server Error", 500

# ========== Start App and Metrics Server ==========
if __name__ == "__main__":
    start_http_server(8000)  # Prometheus scrapes metrics here
    app.run(host="0.0.0.0", port=5000)
