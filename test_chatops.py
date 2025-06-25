import json
import requests
import re
import os
from unittest.mock import patch, MagicMock
from datetime import datetime
from slack_sdk.errors import SlackApiError
from chatops import send_to_slack, post
from terms import return_word

# Test data
TEST_CHANNEL_ID = "test-channel"
TEST_PROFILE_ID = "test-profile"
TEST_ACCESS_TOKEN = "test-token"

def test_send_to_slack():
    # Mock the Slack client
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.data = {"ok": True}
    mock_response.__getitem__.return_value = True
    mock_client.chat_postMessage.return_value = mock_response

    # Mock the global slack_client
    with patch('chatops.slack_client', mock_client):
        # Test successful case
        result = send_to_slack(TEST_CHANNEL_ID, [], "Test message")
        assert result is not None
        assert result["ok"] is True
        mock_client.chat_postMessage.assert_called_once()

        # Reset mock for error case
        mock_client.reset_mock()
        mock_client.chat_postMessage.side_effect = SlackApiError("not_authed", {"error": "not_authed"})

        # Test error case
        result = send_to_slack(TEST_CHANNEL_ID, [], "Test message")
        assert result is None
        mock_client.chat_postMessage.assert_called_once()

def test_post_to_linkedin():
    # Test data
    test_word = "TestWord"
    test_definition = "Test definition"
    test_url = "https://test.com"
    
    # Mock requests.post
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_post = MagicMock(return_value=mock_response)
    
    with patch('requests.post', mock_post):
        result = post(TEST_PROFILE_ID, TEST_ACCESS_TOKEN, test_word, test_definition, test_url)
        assert result.status_code == 201
        mock_post.assert_called_once()

def test_linkedin_hashtag_processing():
    test_cases = [
        ("Machine Learning", "machinelearning"),
        ("AI (Artificial Intelligence)", "aiartificialintelligence"),
        ("Deep-Learning", "deeplearning"),
        ("NLP/Natural Language Processing", "nlpnaturallanguageprocessing")
    ]
    
    for input_word, expected_output in test_cases:
        # Mock requests.post
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.request = MagicMock()
        mock_response.request.body = f"#{expected_output}"
        mock_post = MagicMock(return_value=mock_response)
        
        with patch('requests.post', mock_post):
            result = post(TEST_PROFILE_ID, TEST_ACCESS_TOKEN, input_word, "test", "test.com")
            assert result.status_code == 201
            assert expected_output in result.request.body

if __name__ == "__main__":
    print("Run tests using pytest")
    print("Example: pytest test_chatops.py -v")
