import os

GEMINI_MODEL = "gemini-2.5-flash"
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT","")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
