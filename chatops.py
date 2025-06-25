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

# Retrieve the access token from the environment variable
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
profile_id = os.getenv("PROFILE_ID")
li_access_token = os.getenv("LI_ACCESS_TOKEN")

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

    # Command line arguments parsing
    from argparse import ArgumentParser

    # AI Daily Dose Slack channel
    slack_channel = SLACK_CHANNEL_ID or "general"  # Default to general channel if not specified
    
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
                "text": "Let's learn this AI concept! 💬"
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

    # Now let's post our message to Slack
    res = send_to_slack(slack_channel, slack_blocks, f"AI Daily Dose: {word}")
    if res and res["ok"]:
        print(f"{word} was successfully posted to Slack on {datetime.now()}")
    else:
        print("Failed to post to Slack")
        if res:
            print(f"Error: {res.get('error', 'Unknown error')}")

    # post to linkedin
    res2 = post(profile_id, li_access_token, random_word_name, definition, word_url)
    if res2.status_code == 201:
        print(f"{word} was successfully posted to LinkedIn")
    else:
        print("failed with statusCode: %d" % res2.status_code)
