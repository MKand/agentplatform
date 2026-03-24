import os

GEMINI_MODEL = "gemini-2.5-flash"
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
TEMPLATE_NAME = os.getenv("TEMPLATE_NAME", "template1")
FULL_TEMPLATE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/templates/{TEMPLATE_NAME}"
