from slack_work import *
from creds import *
import time
from pprint import pprint

creds = get_himes_house()
pprint (creds)
channel = creds['channel']
token = creds['token']
 
commands_to_watch_for = [
    'help',
    'tshoot_network']

while 1==1:
    message = get_last_message(token, channel)
    for command in commands_to_watch_for:
        if message in command:
            if 'tshoot_network' in message:
                all_data = tshoot_network(username, password)
                post_to_slack(str(all_data), channel, token)
                post_to_slack('done', channel, token)
    time.sleep(1)

