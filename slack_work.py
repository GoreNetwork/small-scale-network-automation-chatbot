# build_out bot permissions @ https://api.slack.com/apps/A019R6FPY90/oauth?success=1
import slack
import requests
def post_to_slack(message, channel, token):
    slack_token = token
    client = slack.WebClient(token=slack_token)
    client.chat_postMessage(
    channel = channel,
    text=message)

def get_last_message(token, channel):
    url = 'https://slack.com/api/conversations.history?token={}&channel={}&limit=1&pretty=1'.format(token, channel)
    r = requests.get(url)
    all_response = r.json()
    last_message = all_response['messages'][0]['text']
    return last_message    


