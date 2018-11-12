
import os 
from slackclient import SlackClient

token = "xoxb-456010550053-478476771575-QwWRMkKl99HQcdIBKhQFJvdD"

slack_client = SlackClient(token)

bool = slack_client.rtm_connect(with_team_state=True)

# slack_client.api_call("chat.postMessage", channel="C0")

#Connect to slack
if bool:
    events = slack_client.rtm_read()

print(bool)

