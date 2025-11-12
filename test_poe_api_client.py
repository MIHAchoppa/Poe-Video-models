#!/usr/bin/env python3
"""
Unit tests for the Poe API Client.
These tests verify the client's functionality without making actual API calls.
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add current directory to path (noqa: E402)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from poe_api_client import PoeAPIClient  # noqa: E402


class TestPoeAPIClient(unittest.TestCase):
    """Test cases for PoeAPIClient."""

    def setUp(self):
        """Set up test fixtures."""
        # Clear environment variable
        if 'POE_API_KEY' in os.environ:
            self.original_key = os.environ['POE_API_KEY']
            del os.environ['POE_API_KEY']
        else:
            self.original_key = None

    def tearDown(self):
        """Clean up after tests."""
        if self.original_key:
            os.environ['POE_API_KEY'] = self.original_key
        elif 'POE_API_KEY' in os.environ:
            del os.environ['POE_API_KEY']

    def test_init_without_api_key_raises_error(self):
        """Test that initialization without API key raises ValueError."""
        with self.assertRaises(ValueError) as context:
            PoeAPIClient()

        self.assertIn("POE_API_KEY", str(context.exception))

    def test_init_with_api_key_parameter(self):
        """Test initialization with API key as parameter."""
        api_key = "test_api_key_123"
        client = PoeAPIClient(api_key=api_key)

        self.assertEqual(client.api_key, api_key)
        self.assertEqual(client.headers["Authorization"], f"Bearer {api_key}")
        self.assertEqual(client.headers["Content-Type"], "application/json")

    def test_init_with_environment_variable(self):
        """Test initialization with API key from environment."""
        api_key = "env_test_key_456"
        os.environ['POE_API_KEY'] = api_key

        client = PoeAPIClient()

        self.assertEqual(client.api_key, api_key)
        self.assertEqual(client.headers["Authorization"], f"Bearer {api_key}")

    def test_base_url(self):
        """Test that base URL is correct."""
        self.assertEqual(PoeAPIClient.BASE_URL, "https://api.poe.com/v1")

    @patch('poe_api_client.requests.post')
    def test_chat_completion_request_structure(self, mock_post):
        """Test that chat_completion makes correct request structure."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "test", "choices": []}
        mock_post.return_value = mock_response

        # Create client
        client = PoeAPIClient(api_key="test_key")

        # Make request
        model = "cole-bennet-gpt"
        messages = [{"role": "user", "content": "Hello world"}]

        client.chat_completion(model, messages)

        # Verify the request
        mock_post.assert_called_once()
        call_args = mock_post.call_args

        # Check URL
        self.assertEqual(call_args[0][0], "https://api.poe.com/v1/chat/completions")

        # Check headers
        self.assertEqual(call_args[1]['headers']['Authorization'], "Bearer test_key")
        self.assertEqual(call_args[1]['headers']['Content-Type'], "application/json")

        # Check payload
        self.assertEqual(call_args[1]['json']['model'], model)
        self.assertEqual(call_args[1]['json']['messages'], messages)

    @patch('poe_api_client.requests.post')
    def test_chat_completion_with_cole_bennet_gpt(self, mock_post):
        """Test chat completion specifically with cole-bennet-gpt model."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": "chatcmpl-123",
            "object": "chat.completion",
            "created": 1677652288,
            "model": "cole-bennet-gpt",
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Hello! How can I help you today?"
                },
                "finish_reason": "stop"
            }]
        }
        mock_post.return_value = mock_response

        # Create client
        client = PoeAPIClient(api_key="test_key")

        # Make the exact request from the problem statement
        response = client.chat_completion(
            model="cole-bennet-gpt",
            messages=[{"role": "user", "content": "Hello world"}]
        )

        # Verify response
        self.assertEqual(response['model'], "cole-bennet-gpt")
        self.assertIn('choices', response)

    @patch('poe_api_client.requests.post')
    def test_chat_completion_handles_api_error(self, mock_post):
        """Test that API errors are handled properly."""
        import requests

        # Setup mock to raise an exception
        mock_post.side_effect = requests.exceptions.RequestException("API Error")

        # Create client
        client = PoeAPIClient(api_key="test_key")

        # Verify error is raised
        with self.assertRaises(requests.exceptions.RequestException):
            client.chat_completion("cole-bennet-gpt", [{"role": "user", "content": "test"}])


if __name__ == '__main__':
    unittest.main()
