# Poe Video Models

The most amazing fine-tuned video generators on the net, accessible via Poe API!

## Overview

This repository demonstrates how to use video generation models through Poe's API. It provides both JavaScript (Node.js) and Python implementations with examples for multiple video models.

## Available Models

- **Sora-Easy**: Video generation model accessible through the Poe API
- **free-video-generator**: Free video generation model accessible through the Poe API
- **Sora2-South-Park**: A fine-tuned video generation model with South Park styling
- **cole-bennet-gpt**: A video generation model designed for video-related tasks

## Prerequisites

### For JavaScript/Node.js
- Node.js installed
- npm package manager

### For Python
- Python 3.6 or higher
- `requests` library (install with `pip install requests`)

### General
- A valid Poe API key from [Poe](https://poe.com)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MIHAchoppa/Poe-Video-models.git
cd Poe-Video-models
```

2. Install dependencies:

**For JavaScript:**
```bash
npm install
```

**For Python:**
```bash
pip install -r requirements.txt
```

3. Set up your Poe API key:
```bash
export POE_API_KEY="your_api_key_here"
```

## Usage

### JavaScript/Node.js Example

The repository includes a Node.js example using the OpenAI SDK:

```javascript
const { OpenAI } = require("openai");

const client = new OpenAI({
    apiKey: process.env.POE_API_KEY, // or "YOUR_POE_API_KEY"
    baseURL: "https://api.poe.com/v1",
});

const chat = await client.chat.completions.create({
    model: "Sora2-South-Park",
    messages: [{ role: "user", content: "Hello world" }],
});

console.log(chat.choices[0].message.content);
```

**Running the JavaScript example:**
```bash
node example.js
```

### Python Example

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

**Running Python examples:**
```bash
python3 examples.py
```

### Using curl

The repository includes a shell script that demonstrates the exact curl command:

```bash
./poe_api_request.sh
```

Or run the curl command directly for any of the available models:

**Example: Using Sora-Easy Model**

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "Sora-Easy",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

**Example: Using free-video-generator Model**

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "free-video-generator",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

**Example: Using Sora2-South-Park Model**

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "Sora2-South-Park",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

**Example: Using cole-bennet-gpt Model**

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "cole-bennet-gpt",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

## API Configuration

The Poe API is compatible with the OpenAI SDK. Configure the client with:
- **apiKey**: Your Poe API key
- **baseURL**: `https://api.poe.com/v1`

### API Endpoint

- **URL**: `https://api.poe.com/v1/chat/completions`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `Authorization: Bearer $POE_API_KEY`
- **Body**:
  ```json
  {
    "model": "model-name",
    "messages": [{"role": "user", "content": "your prompt here"}]
  }
  ```

## Request Format

```json
{
    "model": "model-name",
    "messages": [
        {
            "role": "user",
            "content": "your prompt here"
        }
    ]
}
```

## Model Parameters

When creating a video generation request, you can specify:
- **model**: The name of the video model (e.g., "Sora-Easy", "free-video-generator", "Sora2-South-Park", "cole-bennet-gpt")
- **messages**: An array of message objects with `role` and `content`

## Notes

- Replace `"Hello world"` with your actual video generation prompt
- All models accept the same API format
- Ensure your API key has the necessary permissions to access these models

## Files

### JavaScript Files
- `example.js` - Node.js example using OpenAI SDK
- `package.json` - Node.js dependencies

### Python Files
- `poe_api_client.py` - Python client library for the Poe API
- `examples.py` - Python usage examples
- `test_poe_api_client.py` - Tests for the Python client
- `requirements.txt` - Python dependencies

### Shell Scripts
- `poe_api_request.sh` - Shell script with curl command example

### Documentation
- `README.md` - This documentation file
- `IMPLEMENTATION_SUMMARY.md` - Implementation details

## License

MIT
