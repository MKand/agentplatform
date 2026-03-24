import google.oauth2.id_token

def get_bearer_token(audience: str) -> str:
    try:
        # This will work when deployed to Cloud Run / Compute Engine
        request = Request()
        return google.oauth2.id_token.fetch_id_token(request, audience)
    except Exception as e:
        logger.error(f"Failed to fetch bearer token: {e}")
        return None