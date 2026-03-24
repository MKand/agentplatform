import os
import logging

logger = logging.getLogger(__name__)


def get_bearer_token(audience: str) -> str:
    try:
        import google.oauth2.id_token
        from google.auth.transport.requests import Request
        request = Request()
        return google.oauth2.id_token.fetch_id_token(request, audience)
    except Exception as e:
        logger.warning(f"Could not fetch bearer token (may not be on GCP): {e}")
        return ""
