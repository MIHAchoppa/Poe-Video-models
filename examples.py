#!/usr/bin/env python3
"""
Example usage of the Poe API Client with different scenarios.
"""

from poe_api_client import PoeAPIClient
import json


def example_simple_message():
    """Example: Simple message to cole-bennet-gpt model."""
    print("=" * 60)
    print("Example 1: Simple 'Hello world' message")
    print("=" * 60)

    client = PoeAPIClient()

    response = client.chat_completion(
        model="cole-bennet-gpt",
        messages=[{"role": "user", "content": "Hello world"}]
    )

    print(json.dumps(response, indent=2))
    print()


def example_video_query():
    """Example: Video-related query."""
    print("=" * 60)
    print("Example 2: Video-related query")
    print("=" * 60)

    client = PoeAPIClient()

    response = client.chat_completion(
        model="cole-bennet-gpt",
        messages=[{
            "role": "user",
            "content": "How do I create an engaging music video?"
        }]
    )

    print(json.dumps(response, indent=2))
    print()


def example_multi_turn_conversation():
    """Example: Multi-turn conversation."""
    print("=" * 60)
    print("Example 3: Multi-turn conversation")
    print("=" * 60)

    client = PoeAPIClient()

    response = client.chat_completion(
        model="cole-bennet-gpt",
        messages=[
            {"role": "user", "content": "What are the key elements of videography?"},
            {"role": "assistant", "content": "Key elements include lighting, framing, and storytelling."},
            {"role": "user", "content": "Tell me more about lighting techniques"}
        ]
    )

    print(json.dumps(response, indent=2))
    print()


def main():
    """Run all examples."""
    print("\nPoe API Client Examples\n")

    try:
        # Run example 1: Simple message (matching the curl command)
        example_simple_message()

        # Uncomment to run additional examples:
        # example_video_query()
        # example_multi_turn_conversation()

    except ValueError as e:
        print(f"Error: {e}")
        print("\nPlease set your POE_API_KEY environment variable:")
        print("  export POE_API_KEY=your_api_key_here")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
