from datetime import datetime
from typing import Dict


def build_payload(*, prompt: str) -> Dict[str, str]:
    return {
        "prompt": prompt,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "source": "fullstack-example",
    }
