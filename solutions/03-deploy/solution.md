# Challenge 3: Deploy to Agent Engine - Solution

## What We Added

Cloud deployment with observability and identity management.

## New Files

### `deploy.py`

Deployment script using Vertex AI Agent Engine:

```python
import vertexai
from vertexai import agent_engines

vertexai.init(project=settings.PROJECT_ID, location=settings.LOCATION)

remote_agent = agent_engines.create(
    source_packages=["./fun_agent"],
    entrypoint_module="fun_agent.agent",
    entrypoint_object="root_agent",
    requirements_file="requirements.txt",
    identity_type="SERVICE_ACCOUNT",
    env_vars=env_vars,
    agent_framework="ADK",
)
```

## Key Configuration

### Environment Variables
```python
env_vars = {
    "GOOGLE_GENAI_USE_VERTEXAI": "TRUE",
    "GOOGLE_CLOUD_PROJECT": settings.PROJECT_ID,
    "GOOGLE_CLOUD_LOCATION": settings.LOCATION,
    "TEMPLATE_NAME": settings.TEMPLATE_NAME,
}
```

### Identity Type
- `SERVICE_ACCOUNT`: Uses a dedicated service account for API access
- Enables proper IAM permissions for Model Armor and other GCP services

## Prerequisites

1. Enable Agent Engine API:
   ```bash
   gcloud services enable agentengine.googleapis.com
   ```

2. Grant required IAM roles to your service account:
   ```bash
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:your-sa@$PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/aiplatform.user"
   ```

## Deployment

```bash
python deploy.py
```

The command returns an agent resource name you can use to interact with the deployed agent.

## Observability

Agent Engine automatically integrates with:
- Cloud Monitoring (metrics)
- Cloud Logging (structured logs)
- Cloud Trace (request tracing)

View logs in Cloud Console under Vertex AI → Agent Engine → your agent.

## Next Steps

Proceed to Challenge 4 to add MCP tool integration.
