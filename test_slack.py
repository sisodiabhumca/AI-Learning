#!/usr/bin/env python3
"""
Test script for Slack integration
Run this to test if your Slack bot is configured correctly
"""

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def test_slack_connection():
    """Test the Slack bot connection and permissions"""
    
    # Get environment variables
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    channel_id = os.getenv("SLACK_CHANNEL_ID", "general")
    
    if not slack_token:
        print("❌ SLACK_BOT_TOKEN not found in environment variables")
        return False
    
    print(f"🔧 Testing Slack connection...")
    print(f"📝 Channel: {channel_id}")
    
    # Initialize Slack client
    client = WebClient(token=slack_token)
    
    try:
        # Test authentication
        auth_test = client.auth_test()
        print(f"✅ Bot authenticated as: {auth_test['user']}")
        print(f"✅ Team: {auth_test['team']}")
        
        # Test posting a message
        test_message = "🤖 AI Daily Dose Bot Test - If you see this, the bot is working correctly!"
        
        response = client.chat_postMessage(
            channel=channel_id,
            text=test_message,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "🤖 *AI Daily Dose Bot Test*\n\nIf you see this message, your Slack bot is configured correctly!"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "The bot is ready to post daily AI terms! 🎉"
                    }
                }
            ]
        )
        
        if response["ok"]:
            print("✅ Test message posted successfully!")
            print("✅ Slack integration is working correctly")
            return True
        else:
            print(f"❌ Failed to post message: {response.get('error', 'Unknown error')}")
            return False
            
    except SlackApiError as e:
        print(f"❌ Slack API Error: {e.response['error']}")
        if e.response['error'] == 'token_revoked':
            print("💡 Your bot token may have been revoked. Please check your Slack app settings.")
        elif e.response['error'] == 'channel_not_found':
            print("💡 Channel not found. Make sure the bot is invited to the channel.")
        elif e.response['error'] == 'not_in_channel':
            print("💡 Bot is not in the channel. Please invite the bot to the channel.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_environment_setup():
    """Test if all required environment variables are set"""
    print("🔍 Checking environment variables...")
    
    required_vars = {
        "SLACK_BOT_TOKEN": "Slack Bot OAuth Token",
        "SLACK_CHANNEL_ID": "Slack Channel ID (optional, defaults to 'general')"
    }
    
    optional_vars = {
        "LI_ACCESS_TOKEN": "LinkedIn API Token",
        "PROFILE_ID": "LinkedIn Profile ID"
    }
    
    all_good = True
    
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {description} - Set")
        else:
            print(f"❌ {var}: {description} - Not set")
            if var == "SLACK_BOT_TOKEN":
                all_good = False
    
    print("\n📋 Optional variables:")
    for var, description in optional_vars.items():
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {description} - Set")
        else:
            print(f"⚠️  {var}: {description} - Not set (LinkedIn posting will be skipped)")
    
    return all_good

if __name__ == "__main__":
    print("🚀 AI Daily Dose - Slack Integration Test")
    print("=" * 50)
    
    # Test environment setup
    env_ok = test_environment_setup()
    
    if env_ok:
        print("\n" + "=" * 50)
        # Test Slack connection
        slack_ok = test_slack_connection()
        
        if slack_ok:
            print("\n🎉 All tests passed! Your AI Daily Dose bot is ready to go!")
            print("💡 The bot will post daily AI terms to your Slack channel.")
        else:
            print("\n❌ Slack integration test failed. Please check your configuration.")
    else:
        print("\n❌ Environment setup incomplete. Please set the required environment variables.")
    
    print("\n📚 For setup instructions, see the README.md file.") 