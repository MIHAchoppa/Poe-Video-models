# Poe Video Models

The most amazing fine-tuned video generators on the net, accessible via Poe API!

## Overview

This repository demonstrates how to use fine-tuned video generation models through Poe's API using the OpenAI SDK. These models allow you to generate high-quality videos using natural language prompts.

## Available Models

- **Sora2-SOuth-PArk**: A fine-tuned video generation model with South Park styling

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MIHAchoppa/Poe-Video-models.git
cd Poe-Video-models
```

2. Install dependencies:
```bash
npm install
```

3. Set up your Poe API key:
   - Get your API key from [Poe](https://poe.com)
   - Set it as an environment variable:
     ```bash
     export POE_API_KEY="your_api_key_here"
     ```
   - Or replace `YOUR_POE_API_KEY` in the example code

## Usage

### Basic Example

```javascript
const { OpenAI } = require("openai");

const client = new OpenAI({
    apiKey: "YOUR_POE_API_KEY", // or process.env.POE_API_KEY
    baseURL: "https://api.poe.com/v1",
});

const chat = await client.chat.completions.create({
    model: "Sora2-SOuth-PArk",
    messages: [{ role: "user", content: "Hello world" }],
});

console.log(chat.choices[0].message.content);
```

### Running the Example

```bash
node example.js
```

## API Configuration

The Poe API is compatible with the OpenAI SDK. Simply configure the client with:
- **apiKey**: Your Poe API key
- **baseURL**: `https://api.poe.com/v1`

## Model Parameters

When creating a video generation request, you can specify:
- **model**: The name of the video model (e.g., "Sora2-SOuth-PArk")
- **messages**: An array of message objects with `role` and `content`

## License

MIT
