my-app/
├── base/
│   ├── kustomization.yaml         # ← your current base
│   ├── values.yaml
│   ├── deployment-patch.yaml
├── overlays/
│   └── prod/
│       ├── kustomization.yaml     # ← overlay on top of base
│       └── image-patch.yaml       # optional override
