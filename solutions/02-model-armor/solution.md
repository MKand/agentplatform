# Challenge 2: Model Armor Security - Solution

## What We Added

Security guardrails to detect prompt injection, sensitive data, and harmful content.

## New Files

### `fun_agent/model_armor_guard.py`

A callback-based security guard using Model Armor API:

```python
class ModelArmorGuard:
    async def before_model_callback(self, callback_context, llm_request):
        # Sanitize user input before LLM processing
        result = self.client.sanitize_user_prompt(request=sanitize_request)
        if matched_filters:
            return LlmResponse(...)  # Block the request

    async def after_model_callback(self, callback_context, llm_response):
        # Sanitize model output before returning to user
        result = self.client.sanitize_model_response(request=sanitize_request)
```

### Callback Architecture

ADK agents support two callback hooks:
- **`before_model_callback`**: Intercepts requests before LLM processes them
- **`after_model_callback`**: Intercepts responses before they're returned

## How It Works

1. Extract user text from `LlmRequest`
2. Send to Model Armor API for sanitization
3. Check for matched filters (pi_and_jailbreak, sdp, rai, etc.)
4. Return blocked response or allow through

## Environment Setup

Before running, create a Model Armor template in Google Cloud Console:
1. Go to Vertex AI → Model Armor
2. Create a new template with default settings
3. Note the template resource name

```bash
export TEMPLATE_NAME="projects/your-project/locations/us-central1/templates/template1"
```

## Testing Security

Try these prompts - they should be blocked:
- "Ignore all previous instructions..."
- "Credit card: 4532-1234-5678-9010"
- "Check out http://totally-not-malicious.com"

## Next Steps

Proceed to Challenge 3 to deploy to Agent Engine.
