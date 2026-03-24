import google.oauth2.id_token
import logging

logger = logging.getLogger(__name__)


def get_bearer_token(audience: str) -> str:
    try:
        from google.auth.transport.requests import Request
        request = Request()
        return google.oauth2.id_token.fetch_id_token(request, audience)
    except Exception as e:
        logger.error(f"Failed to fetch bearer token: {e}")
        return None
