# Challenge 3: Deploy to Agent Engine - Solution

## What We Added

Cloud deployment with observability and identity management.

## New Files

### `deploy.sh`

Deployment script using the ADK CLI:

```bash
#!/bin/bash
set -e

echo "Authenticating with GCP..."
gcloud auth application-default login
gcloud auth login
gcloud auth application-default set-quota-project "$GOOGLE_CLOUD_PROJECT"

STAGING_BUCKET="gs://$GOOGLE_CLOUD_PROJECT-ae-staging-bucket"

echo "Creating staging bucket if it doesn't exist..."
gcloud storage buckets create "$STAGING_BUCKET" --project="$GOOGLE_CLOUD_PROJECT" --location="$GOOGLE_CLOUD_LOCATION" 2>/dev/null || echo "Bucket already exists"

echo "Deploying agent to Agent Engine..."
adk deploy agent_engine fun_agent \
    --project="$GOOGLE_CLOUD_PROJECT" \
    --region="$GOOGLE_CLOUD_LOCATION" \
    --display_name="Fun Agent" \
    --staging_bucket="$STAGING_BUCKET" \
    --trace_to_cloud \
    --env_file="fun_agent/.env"
```

## Key Configuration

### Environment Variables (`.env` file)
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
TEMPLATE_NAME=your-template-name
```

### Flags
- `--trace_to_cloud`: Enables Cloud Trace for observability
- `--env_file`: Loads environment variables from file

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
chmod +x deploy.sh
./deploy.sh
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
