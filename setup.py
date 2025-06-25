#!/usr/bin/env python3
"""
AI Daily Dose - Slack Bot Setup Script
This script helps you set up your Slack bot configuration
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create a .env file from the example"""
    example_file = Path("config.example.env")
    env_file = Path(".env")
    
    if env_file.exists():
        print("⚠️  .env file already exists. Skipping creation.")
        return
    
    if example_file.exists():
        with open(example_file, 'r') as f:
            content = f.read()
        
        with open(env_file, 'w') as f:
            f.write(content)
        
        print("✅ Created .env file from config.example.env")
        print("📝 Please edit .env file with your actual values")
    else:
        print("❌ config.example.env not found")

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    try:
        import slack_sdk
        print("✅ slack-sdk installed")
    except ImportError:
        print("❌ slack-sdk not installed")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    try:
        import requests
        print("✅ requests installed")
    except ImportError:
        print("❌ requests not installed")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    try:
        import tinydb
        print("✅ tinydb installed")
    except ImportError:
        print("❌ tinydb not installed")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    return True

def print_setup_instructions():
    """Print setup instructions"""
    print("\n" + "="*60)
    print("🚀 AI Daily Dose - Slack Bot Setup Instructions")
    print("="*60)
    
    print("\n📋 Step 1: Create a Slack App")
    print("   1. Go to https://api.slack.com/apps")
    print("   2. Click 'Create New App' → 'From scratch'")
    print("   3. Name your app (e.g., 'AI Daily Dose Bot')")
    print("   4. Select your workspace")
    
    print("\n📋 Step 2: Configure Bot Permissions")
    print("   1. Go to 'OAuth & Permissions' in the left sidebar")
    print("   2. Add these scopes:")
    print("      - chat:write")
    print("      - chat:write.public")
    print("   3. Click 'Install to Workspace'")
    print("   4. Copy the 'Bot User OAuth Token' (starts with xoxb-)")
    
    print("\n📋 Step 3: Get Channel ID")
    print("   1. Right-click on your target channel in Slack")
    print("   2. Select 'Copy link' and extract the channel ID")
    print("   3. Or use the channel name (e.g., '#general')")
    
    print("\n📋 Step 4: Configure Environment Variables")
    print("   1. Edit the .env file with your values:")
    print("      SLACK_BOT_TOKEN=xoxb-your-token-here")
    print("      SLACK_CHANNEL_ID=your-channel-id")
    
    print("\n📋 Step 5: Test Your Setup")
    print("   Run: python test_slack.py")
    
    print("\n📋 Step 6: Run the Bot")
    print("   Run: python chatops.py")
    
    print("\n📋 Step 7: Set up GitHub Actions (Optional)")
    print("   1. Go to your repository → Settings → Secrets")
    print("   2. Add the same environment variables as secrets")
    print("   3. The bot will run daily at 9 AM EST")
    
    print("\n" + "="*60)
    print("🎉 Happy AI learning!")
    print("="*60)

def main():
    """Main setup function"""
    print("🤖 AI Daily Dose - Slack Bot Setup")
    print("="*40)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Please install dependencies first:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Print instructions
    print_setup_instructions()

if __name__ == "__main__":
    main() 