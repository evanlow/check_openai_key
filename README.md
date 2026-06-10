# check_openai_key

A simple Flask web app that lets you verify whether an OpenAI API key is active and valid — without consuming generation tokens.

## Features

- Paste any OpenAI API key and instantly check its status
- Uses the `models.list()` endpoint to validate the key without consuming generation tokens (though the request may still count against rate limits)
- Distinguishes between invalid/inactive keys and permission errors
- Clean, minimal UI

## Requirements

- Python 3.9+
- An internet connection to reach the OpenAI API

## Installation

```bash
# Clone the repository
git clone https://github.com/evanlow/check_openai_key.git
cd check_openai_key

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser, paste your OpenAI API key, and click **Check Key**.

### Debug mode

```bash
FLASK_DEBUG=true python app.py
```

## How it works

1. You submit an API key via the web form.
2. The server creates an OpenAI client with that key and calls `client.models.list()`.
3. The result is shown immediately:
   - ✅ **Active** — the key is valid and usable.
   - ❌ **Inactive / Invalid** — authentication failed (key is revoked, expired, or incorrect).
   - 🔒 **Permission Denied** — the key is valid but lacks required permissions.
   - ⚠️ **Error** — an unexpected error occurred.

## Security note

Your API key is sent to the server only to make the validation request and is not intentionally stored or logged by this application.