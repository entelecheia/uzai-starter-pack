"""Shared helper reused by Azure Functions samples."""

import json
from datetime import datetime
from typing import Dict


def generate_response(*, user_message: str, deployment: str) -> str:
    """Pretend to call Azure OpenAI and return a JSON string."""
    payload: Dict[str, str] = {
        "deployment": deployment,
        "message": user_message,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
    return json.dumps(payload)
