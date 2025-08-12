from typing import Any
import httpx
from fastmcp import FastMCP, Context
from fastmcp.types import TextContent

# Initialize FastMCP server
mcp = FastMCP(name="WeatherDemoServer")

# Constants for weather API
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

# Tool to fetch weather data
@mcp.tool()
async def get_weather(city: str, ctx: Context) -> str:
    """Fetch current weather for a given city using National Weather Service API."""
    try:
        async with httpx.AsyncClient() as client:
            # Example: Using a simplified approach for demo purposes
            # In production, you'd need to geocode the city to lat/lon
            response = await client.get(
                f"{NWS_API_BASE}/points/40.7128,-74.0060/forecast",  # Example: New York City
                headers={"User-Agent": USER_AGENT}
            )
            response.raise_for_status()
            data = response.json()
            forecast = data["properties"]["periods"][0]["detailedForecast"]
            await ctx.info(f"Retrieved weather for {city}: {forecast}")
            return f"Weather in {city}: {forecast}"
    except httpx.HTTPError as e:
        await ctx.error(f"Failed to fetch weather: {str(e)}")
        return f"Error fetching weather for {city}: {str(e)}"

# Tool for basic calculation
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Resource: Sample weather data
@mcp.resource()
def sample_weather_data() -> str:
    """Provide sample weather data as a resource."""
    return """Sample Weather Data:
City: New York
Temperature: 72°F
Condition: Partly cloudy"""

# Prompt: Guide LLM response formatting
@mcp.prompt()
def weather_prompt(city: str) -> str:
    """Prompt template for weather queries."""
    return f"Provide a concise weather summary for {city}. Include temperature, conditions, and any notable weather events."

# Run the server
if __name__ == "__main__":
    mcp.run()