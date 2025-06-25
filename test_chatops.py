import json
import requests
import re
import time
import subprocess
import os
from test_terms import return_word
from datetime import datetime


# Retrieve the environment variables
TEAMS_ACCESS_TOKEN = os.getenv("TEAMS_ACCESS_TOKEN")
profile_id = os.getenv("PROFILE_ID")
li_access_token = os.getenv("LI_ACCESS_TOKEN")

if TEAMS_ACCESS_TOKEN:
    print("Access token retrieved successfully")
else:
    print("Failed to retrieve access token")


# Simple Bot Function for passing messages to a room
def send_it(token, room_id, message):

    header = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}

    data = {"roomId": room_id, "text": message, "attachments": card}

    return requests.post(
        "https://api.ciscospark.com/v1/messages/",
        headers=header,
        data=json.dumps(data),
        verify=True,
    )


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
    random_word_linkedin = re.sub("\(.*?\)", "()", random_word_linkedin)
    # remove (), -.  and /
    random_word_linkedin = random_word_linkedin.replace("(", "").replace(")", "")
    random_word_linkedin = random_word_linkedin.replace("-", "").replace("/", "")
    random_word_linkedin = random_word_linkedin.replace(".", "")
    post_data = {
        "author": "urn:li:person:" + profile_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": f"-------------\nAI Daily Dose\n-------------\n\n\n{random_word_name}\n\n\n{definition}\n\n\n#Tech #AIDailyDose #{random_word_linkedin} #AI #ArtificialIntelligence\n\nThis automated post was created using #Python and a LinkedIn #API. Feel free to share related resources and/or discuss this topic in the comments. Anyone can join the Webex space for the AI Daily Dose: https://eurl.io/#vPEHI7XF1"
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

    # Bot Testing room
    teams_room = (
        "Y2lzY29zcGFyazovL3VzL1JPT00vMTM4YTljMzAtNGI4NS0xMWYwLTk4NDEtZjUwZGUyZThiZjli"
    )

    the_message = ""
    # fetch random dictionary containing word as key and definition as value
    random_word = return_word()
    random_word_name = random_word["name"]
    word = "\n" + random_word["name"] + "\n"
    word_url = random_word["url"]
    definition = random_word["definition"]
    wiki_link_text = f"Click to Learn about '{random_word_name}'"

    card = [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "version": "1.2",
                "body": [
                    # {
                    #     "type": "Image",
                    #     "url": "https://raw.githubusercontent.com/xanderstevenson/word-of-the-day/main/media/AI-Webex-500.png",  # Replace with your image URL
                    #     "horizontalAlignment": "center",
                    #     "width": "100px",
                    #     "height": "100px",
                    # },
                    {
                        "type": "TextBlock",
                        "text": "AI Daily Dose",
                        "size": "ExtraLarge",
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "color": "Warning",
                        "weight": "Bold",
                        "wrap": True,
                        "style": "Emphasis",
                    },
                    {
                        "type": "TextBlock",
                        "text": word,
                        "size": "ExtraLarge",
                        "separator": True,
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "color": "Good",
                        "weight": "Bolder",
                        "wrap": True,
                    },
                    {
                        "type": "TextBlock",
                        "text": definition,
                        "size": "Medium",
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "wrap": True,
                    },
                    {
                        "type": "ActionSet",
                        "horizontalAlignment": "center",
                        "actions": [
                            {
                                "type": "Action.OpenUrl",
                                "url": word_url,
                                "title": wiki_link_text,
                                "style": "positive",
                                "horizontalAlignment": "center",
                            }
                        ],
                    },
                    {
                        "type": "TextBlock",
                        "text": "Reply below and let's discuss this AI concept!",
                        "size": "Small",
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "wrap": True,
                        "color": "Warning",
                    },
                ],
            },
        }
    ]

    # Now let's post our message to Webex Teams
    res = send_it(TEAMS_ACCESS_TOKEN, teams_room, the_message)
    if res.status_code == 200:
        print(f"{word} was successfully posted to Webex Teams on {datetime.now()}")

    else:
        print("Failed with status code: %d" % res.status_code)
        if res.status_code == 404:
            print(
                "Please check that the bot is in the room you're attempting to post to..."
            )
        elif res.status_code == 400:
            print(
                "Please check the identifier of the room you're attempting to post to..."
            )
        elif res.status_code == 401:
            print("Please check if the access token is correct...")

    # post to linkedin
    
    # res2 = post(profile_id, li_access_token, random_word_name, definition, word_url)
    # if res2.status_code == 201:
    #     print(f"{word} was successfully posted to LinkedIn")
    # else:
    #     print("failed with statusCode: %d" % res2.status_code)
