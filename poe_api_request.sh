#!/bin/bash

# Poe API Request Script
# This script demonstrates the curl command to interact with the Poe API

# Check if POE_API_KEY is set
if [ -z "$POE_API_KEY" ]; then
    echo "Error: POE_API_KEY environment variable is not set"
    echo "Please set it with: export POE_API_KEY=your_api_key_here"
    exit 1
fi

# Make the API request
curl "https://api.poe.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $POE_API_KEY" \
    -d '{
        "model": "cole-bennet-gpt",
        "messages": [{"role": "user", "content": "Hello world"}]
    }'
