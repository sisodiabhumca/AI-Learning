import json
import requests
import re
import time
import subprocess
import os
from terms import return_word
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import sys

# Debug function to print environment variables safely
def debug_env_vars():
    print("\n=== Environment Variables Debug ===")
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Available environment variables:")
    for key in sorted(os.environ):
        if key.startswith("SLACK") or key.startswith("LI") or key == "PROFILE_ID":
            print(f"{key}: {bool(os.environ.get(key))}")
    print("=== End of Debug ===\n")

# Call debug function immediately
debug_env_vars()

# Retrieve the access token from the environment variable
# SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
# SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
SLACK_BOT_TOKEN=xoxb-4341754681251-9097444536725-HSEjiWcOXtRkBMQlXkQhIg7E
SLACK_CHANNEL_ID=D092X4B21QA
profile_id = os.getenv("PROFILE_ID")
li_access_token = os.getenv("LI_ACCESS_TOKEN")

# Debug output for troubleshooting
print("\n=== Environment Variable Debug ===")
print(f"SLACK_BOT_TOKEN: {'Set' if SLACK_BOT_TOKEN else 'Not Set'}")
print(f"SLACK_CHANNEL_ID: {'Set' if SLACK_CHANNEL_ID else 'Not Set'}")
print(f"LI_ACCESS_TOKEN: {'Set' if li_access_token else 'Not Set'}")
print(f"PROFILE_ID: {'Set' if profile_id else 'Not Set'}")

# Print environment variable values (without exposing secrets)
if SLACK_BOT_TOKEN:
    print(f"SLACK_BOT_TOKEN length: {len(SLACK_BOT_TOKEN)}")
if SLACK_CHANNEL_ID:
    print(f"SLACK_CHANNEL_ID length: {len(SLACK_CHANNEL_ID)}")

print("\n=== Environment Variables ===")
for key in sorted(os.environ):
    if key.startswith("SLACK") or key.startswith("LI") or key == "PROFILE_ID":
        value = os.environ[key]
        print(f"{key}: {'Set' if value else 'Not Set'}")
        if value:
            print(f"{key} length: {len(value)}")
print("=== End of Debug ===\n")

# Check if required Slack credentials are set
if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
    print("Error: Slack credentials not properly configured")
    print("Please set SLACK_BOT_TOKEN and SLACK_CHANNEL_ID as GitHub Secrets")
    exit(1)

# Debug output for troubleshooting
print(f"\n=== Credential Debug ===")
print(f"SLACK_BOT_TOKEN is set: {bool(SLACK_BOT_TOKEN)}")
print(f"SLACK_CHANNEL_ID is set: {bool(SLACK_CHANNEL_ID)}")
print(f"LI_ACCESS_TOKEN is set: {bool(li_access_token)}")
print(f"PROFILE_ID is set: {bool(profile_id)}")
print(f"SLACK_BOT_TOKEN length: {len(SLACK_BOT_TOKEN) if SLACK_BOT_TOKEN else 0}")
print(f"SLACK_CHANNEL_ID length: {len(SLACK_CHANNEL_ID) if SLACK_CHANNEL_ID else 0}")
print("=== End of Credential Debug ===\n")

# Debug output for troubleshooting
print(f"SLACK_BOT_TOKEN is set: {bool(SLACK_BOT_TOKEN)}")
print(f"SLACK_CHANNEL_ID is set: {bool(SLACK_CHANNEL_ID)}")
print(f"LI_ACCESS_TOKEN is set: {bool(li_access_token)}")
print(f"PROFILE_ID is set: {bool(profile_id)}")

if SLACK_BOT_TOKEN:
    print("Slack bot token retrieved successfully")
else:
    print("Failed to retrieve Slack bot token")

# Initialize Slack client
slack_client = WebClient(token=SLACK_BOT_TOKEN)

# Slack Bot Function for passing messages to a channel
def send_to_slack(channel_id, blocks, text=""):
    try:
        response = slack_client.chat_postMessage(
            channel=channel_id,
            text=text,
            blocks=blocks
        )
        return response
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
        return None

# post to LinkedIn
# will change to https://api.linkedin.com/rest/posts
def post(profile_id, li_access_token, random_word_name, definition, word_url):

    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + li_access_token,
    }
    # make new variable for linkedin hashtag, lowercase it and remove spaces
    random_word_linkedin = random_word_name.lower().replace(" ", "")
    # remove abbreviations for linkedin hashtag
    # remove everything between ()
    random_word_linkedin = re.sub(r"\(.*?\)", "", random_word_linkedin)
    # remove remaining parentheses, hyphens, slashes, and dots
    random_word_linkedin = re.sub(r'[().\-/\.]', '', random_word_linkedin)
    post_data = {
        "author": "urn:li:person:" + profile_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": f"-------------\nAI Daily Dose\n-------------\n\n\n{random_word_name}\n\n\n{definition}\n\n\n#Tech #AIDailyDose #{random_word_linkedin} #AI #ArtificialIntelligence\n\nThis automated post was created using #Python and a LinkedIn #API. Feel free to share related resources and/or discuss this topic in the comments. Anyone can join the Slack channel for the AI Daily Dose!"
                },
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    response = requests.post(url, headers=headers, json=post_data)
    return response


if __name__ == "__main__":
    # Check if required Slack credentials are set
    if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
        print("Error: Slack credentials not properly configured")
        print("Please set SLACK_BOT_TOKEN and SLACK_CHANNEL_ID as GitHub Secrets")
        exit(1)

    # Check if LinkedIn credentials are set
    has_linkedin_credentials = bool(profile_id and li_access_token)
    
    try:
        # fetch random dictionary containing word as key and definition as value
        random_word = return_word()
        random_word_name = random_word["name"]
        word = random_word["name"]
        word_url = random_word["url"]
        definition = random_word["definition"]
        wiki_link_text = f"Learn about '{random_word_name}'"

        # Create Slack blocks for rich message formatting
        slack_blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🤖 AI Daily Dose",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{word}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": definition
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Reply below and let's discuss this AI concept! 💬"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": wiki_link_text,
                            "emoji": True
                        },
                        "url": word_url,
                        "style": "primary"
                    }
                ]
            }
        ]

        # Post to Slack
        res = send_to_slack(SLACK_CHANNEL_ID, slack_blocks, f"AI Daily Dose: {word}")
        if res and res["ok"]:
            print(f"{word} was successfully posted to Slack on {datetime.now()}")
        else:
            print("Failed to post to Slack")
            if res:
                print(f"Error: {res.get('error', 'Unknown error')}")
            exit(1)

        # Post to LinkedIn if credentials are available
        if has_linkedin_credentials:
            print("Attempting to post to LinkedIn...")
            try:
                res2 = post(profile_id, li_access_token, random_word_name, definition, word_url)
                if res2.status_code == 201:
                    print(f"{word} was successfully posted to LinkedIn")
                else:
                    print(f"Failed to post to LinkedIn with status code: {res2.status_code}")
            except Exception as e:
                print(f"Error posting to LinkedIn: {str(e)}")
        else:
            print("LinkedIn credentials not configured - skipping LinkedIn post")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit(1)
