Creating a demo for small scale automation.  This is a slack chatbot that watches a slack channel for commands, upon getting those commands it will execute a function.  Currently it will do: 
  Some basic trouble shooting such as checking BPG neighbors, NTP sync status, CPU usage, and looks in the log for EIGRP, OSPF flaps, recursion, flapping mac addresses, and Duplicate addresses. Use the command "**tshoot_network**"
       
       Device Name: R1
       CPU Usage: 0%
       NTP Synched: True
       IP: 10.0.0.1
       Time of run: 2020/Aug/29/17:18:22.812: UTC
       BPG issues:
               11.11.11.11 is down
               11.11.11.11 is an extra BGP nei
               12.12.12.12 is missing
  
  Check all interfaces on devices looking for a subnet that an IP is part of:
       **find ip 172.16.1.250**
       
       Device: Home_Switch
               interface Vlan2
               Device IP:  172.16.1.1
               Subnet Mask: 255.255.255.0
       ===========

**Setup credentials:**

To get the credentials you'll need to **edit the file named creds.py** and put in the channel name that you want the bot to watch, and the token you get from the slack page.  The file should look like this

       def get_himes_house():
           creds = {}
           creds['token'] = 'xoxb-blah'
           creds['channel'] = 'C01QKFD8NSH'
           return creds

You can see in line 7 of run_slack_bot.py

       creds = get_himes_house()
This is calling a function that gets the credentials for slack access.  Splitting up the credentials by name can let you store multiple sets of credentials easily.  Just put in your own function with the credentials you want, under the function name you want, and call it in run_slack_bot.



**Getting Slack Token:**

You'll go to https://api.slack.com/apps and click "Create New App"

You'll be asked for an App Name, and what Slack Workspace you want to work in the demo you'll see I am working in Himes_House, and my demo is named Network TS, so that's what I chose.  Fill in your info.  Then hit Create App.  (you can change the display name later if you want)

Under the "OAuth Tokens & Redirect URLs" there is a section called "Bot Token Scopes
".  You'll probably want to add the **OAuth Scopes** 

        calls:read
                View information about ongoing and past calls

        channels:history
                View messages and other content in a user’s public channels

        chat:write
                Send messages on a user’s behalf

        groups:history
                View messages and other content in a user’s private channels

        im:history
                View messages and other content in a user’s direct messages

        mpim:history
                View messages and other content in a user’s group direct messages

After that is done copy out the "Bot User OAuth Token", which should start with xoxb-.  This is also on the same OAuth & Permissions page.

**Getting Channel Data:**

This one is pretty easy: in slack just right click a channel, and select copy link, then the last section of the link is the channel you want.  
Example: in https://himeshouse.slack.com/archives/C01QKFD8NSH  C01QKFD8NSH is the channel key.

**Starting the program:**

Super easy, just run  
*python run_slack_bot.py*