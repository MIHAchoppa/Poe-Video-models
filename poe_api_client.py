#!/usr/bin/env python3
"""
Poe API Client for Video Models
This script demonstrates how to interact with the Poe API chat completions endpoint.
"""

import os
import sys
import json
import requests


class PoeAPIClient:
    """Client for interacting with the Poe API."""

    BASE_URL = "https://api.poe.com/v1"

    def __init__(self, api_key=None):
        """
        Initialize the Poe API client.

        Args:
            api_key: Poe API key. If not provided, will look for POE_API_KEY environment variable.
        """
        self.api_key = api_key or os.environ.get("POE_API_KEY")
        if not self.api_key:
            raise ValueError("POE_API_KEY must be provided or set as environment variable")

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def chat_completion(self, model, messages):
        """
        Send a chat completion request to the Poe API.

        Args:
            model: The model to use (e.g., "cole-bennet-gpt")
            messages: List of message dictionaries with 'role' and 'content' keys

        Returns:
            Response from the API as a dictionary
        """
        url = f"{self.BASE_URL}/chat/completions"

        payload = {
            "model": model,
            "messages": messages
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}", file=sys.stderr)
            if hasattr(e.response, 'text'):
                print(f"Response: {e.response.text}", file=sys.stderr)
            raise


def main():
    """Main function to demonstrate API usage."""
    try:
        # Initialize the client
        client = PoeAPIClient()

        # Use the cole-bennet-gpt model as shown in the curl example
        model = "cole-bennet-gpt"
        messages = [
            {"role": "user", "content": "Hello world"}
        ]

        print(f"Sending request to Poe API with model: {model}")
        print(f"Messages: {json.dumps(messages, indent=2)}\n")

        # Make the API call
        response = client.chat_completion(model, messages)

        # Print the response
        print("Response:")
        print(json.dumps(response, indent=2))

    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        print("\nPlease set your POE_API_KEY environment variable:", file=sys.stderr)
        print("  export POE_API_KEY=your_api_key_here", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
