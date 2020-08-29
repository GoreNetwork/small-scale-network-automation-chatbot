from slack_work import *
from creds import *
import time
from pprint import pprint
from main import *

creds = get_himes_house()
pprint (creds)
channel = creds['channel']
token = creds['token']
 
commands_to_watch_for = [
    'help',
    'tshoot_network']

def network_tshoot_pretty_output(device):
    pprint (device)
    output = '''*********************
*Device Name*: {}
        *CPU Usage:* {}%
        *NTP Synched:* {}
        *IP:* {}
        *Time of run:* {}
'''.format(device['Device Name'],
    device['cpu_usage_percent'],
    device['ntp_working'],
    device['IP'],
    device['current_time'])

    if 'BGP issues' in device:
        output = output+"        *BPG issues:* \n"
        for issue in device['BGP issues']:
            output = output+ "                {}\n".format(issue)


    if len(device['questionable_log_lines']) >0:
        output = "{}        *Issues from log:* \n".format(output)
        for line in device['questionable_log_lines']:
            output = "{}           {}\n".format(output, line)
            for time in device['questionable_log_lines'][line]:
                output = "{}                     {}\n".format(output, time)
        
    return output



while 1==1:
    message = get_last_message(token, channel)
    for command in commands_to_watch_for:
        if message in command:
            if 'tshoot_network' in message:
                all_data = tshoot_network(username, password)
                for device in all_data:
                    output = network_tshoot_pretty_output(device)
                    post_to_slack(output, channel, token)
                post_to_slack('done', channel, token)
    time.sleep(1)

