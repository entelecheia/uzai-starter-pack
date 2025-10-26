import logging
import os
from http import HTTPStatus

import azure.functions as func

from .prompt_bridge import generate_response


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing onboarding demo request")

    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse(
            body="Invalid JSON payload",
            status_code=HTTPStatus.BAD_REQUEST,
        )

    user_message = payload.get("message", "")
    if not user_message:
        return func.HttpResponse("Message is required", status_code=HTTPStatus.BAD_REQUEST)

    deployment = os.environ.get("OPENAI_DEPLOYMENT", "gpt-4o-mini")
    result = generate_response(user_message=user_message, deployment=deployment)

    return func.HttpResponse(
        body=result,
        status_code=HTTPStatus.OK,
        mimetype="application/json",
    )
