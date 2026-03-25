# Challenge 3: Deploy to Agent Engine - Solution

## What We Added

Cloud deployment with observability and identity management.

## Deployment Method: Agent Object

This solution uses **agent object deployment** - passing the `root_agent` directly to `client.agent_engines.create()`:

```python
from fun_agent.agent import root_agent

remote_agent = client.agent_engines.create(
    agent=root_agent,  # Passing the agent object directly
    config={...}
)
```

### How It Works

1. The agent object is serialized to a pickle file (`.pkl`)
2. The pickle file is uploaded to Cloud Storage
3. Agent Engine deserializes and runs the agent

### When to Use This Method

- Simple agents without complex dependencies
- Fast iteration during development
- Agents that can be easily pickled (no non-serializable objects)

## Prerequisites

1. Enable Agent Engine API:

   ```bash
   gcloud services enable agentengine.googleapis.com
   ```

2. Create a staging bucket:

   ```bash
   gcloud storage buckets create "gs://$GOOGLE_CLOUD_PROJECT-ae-staging-bucket" --project="$GOOGLE_CLOUD_PROJECT" --location="$GOOGLE_CLOUD_LOCATION"
   ```

3. Grant required IAM roles to your service account:

   ```bash
   gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member="serviceAccount:your-sa@$PROJECT_ID.iam.gserviceaccount.com" \
     --role="roles/aiplatform.user"
   ```

### Deploy

Run the deployment script:

```bash
cd solutions/03-deploy
python3 deploy.py
```

The command returns an agent resource name you can use to interact with the deployed agent.

## Observability

Agent Engine automatically integrates with:

- Cloud Monitoring (metrics)
- Cloud Logging (structured logs)
- Cloud Trace (request tracing)

View logs in Cloud Console under Vertex AI → Agent Engine → your agent.

## Architecture

```
User → Agent Engine → Agent (ADK) → Model Armor → Gemini
```

## Next Steps

Proceed to Challenge 4 to add MCP tool integration.
