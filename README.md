# Poe-Video-models

This repository provides documentation and examples for using Poe's video generation models through the chat completions API.

## Available Models

### Sora-Easy
A video generation model accessible through the Poe API.

### free-video-generator
A free video generation model accessible through the Poe API.

## API Usage

### Prerequisites
- A valid Poe API key (set as `POE_API_KEY` environment variable)
- curl or any HTTP client

### Example: Using Sora-Easy Model

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "Sora-Easy",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

### Example: Using free-video-generator Model

```bash
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "free-video-generator",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
```

## API Endpoint

- **URL**: `https://api.poe.com/v1/chat/completions`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <YOUR_POE_API_KEY>`

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

## Getting Started

1. Obtain your Poe API key from the Poe platform
2. Set your API key as an environment variable:
   ```bash
   export POE_API_KEY="your-api-key-here"
   ```
3. Use the curl examples above to generate videos with your preferred model

## Notes

- Replace `"Hello world"` with your actual video generation prompt
- Both models accept the same API format
- Ensure your API key has the necessary permissions to access these models