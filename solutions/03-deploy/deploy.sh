#!/bin/bash

set -e

echo "Authenticating with GCP..."
gcloud auth application-default login
gcloud auth login
gcloud auth application-default set-quota-project "$GOOGLE_CLOUD_PROJECT"

STAGING_BUCKET="gs://$GOOGLE_CLOUD_PROJECT-ae-staging-bucket"

echo "Creating staging bucket if it doesn't exist..."
gcloud storage buckets create "$STAGING_BUCKET" --project="$GOOGLE_CLOUD_PROJECT" --location="$GOOGLE_CLOUD_LOCATION" 2>/dev/null || echo "Bucket already exists"

