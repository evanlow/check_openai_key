import logging
import os

from flask import Flask, render_template, request
from openai import OpenAI, AuthenticationError, PermissionDeniedError

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_key():
    api_key = request.form.get("api_key", "").strip()

    if not api_key:
        return render_template(
            "index.html",
            result="error",
            message="Please enter an API key.",
        )

    try:
        client = OpenAI(api_key=api_key)
        # Use models.list() to validate the key without consuming any tokens.
        client.models.list()
        return render_template(
            "index.html",
            result="active",
            message="✅ Key is active and usable.",
        )
    except AuthenticationError:
        return render_template(
            "index.html",
            result="inactive",
            message="❌ Key is inactive or invalid.",
        )
    except PermissionDeniedError:
        return render_template(
            "index.html",
            result="inactive",
            message="❌ Key does not have the required permissions.",
        )
    except Exception:
        logger.exception("Unexpected error while checking API key")
        return render_template(
            "index.html",
            result="error",
            message="⚠️ An unexpected error occurred. Please try again.",
        )


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true", "yes"}
    app.run(debug=debug)
