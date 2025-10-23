# Poe-Video-models

This repository provides tools and examples for interacting with Poe Video Models API, specifically demonstrating the use of the `cole-bennet-gpt` model.

## Prerequisites

- Python 3.6 or higher (for Python script)
- `requests` library (install with `pip install requests`)
- A valid Poe API key

## Setup

Set your Poe API key as an environment variable:

```bash
export POE_API_KEY=your_api_key_here
```

## Usage

### Using the curl command (Shell script)

The repository includes a shell script that demonstrates the exact curl command:

```bash
./poe_api_request.sh
```

Or run the curl command directly:

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "cole-bennet-gpt",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

### Using the Python client

The repository also includes a Python client for easier integration:

```bash
python3 poe_api_client.py
```

Or use it in your own Python code:

```python
from poe_api_client import PoeAPIClient

# Initialize client
client = PoeAPIClient()

# Make a request
response = client.chat_completion(
    model="cole-bennet-gpt",
    messages=[{"role": "user", "content": "Hello world"}]
)

print(response)
```

## API Endpoint

- **URL**: `https://api.poe.com/v1/chat/completions`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `Authorization: Bearer $POE_API_KEY`
- **Body**:
  ```json
  {
    "model": "cole-bennet-gpt",
    "messages": [{"role": "user", "content": "Hello world"}]
  }
  ```

## Models

The repository is configured to use the `cole-bennet-gpt` model by default. This model is designed for video-related tasks.

## Files

- `poe_api_request.sh` - Shell script with the curl command example
- `poe_api_client.py` - Python client library for the Poe API
- `README.md` - This documentation file

## License

See LICENSE file for details.