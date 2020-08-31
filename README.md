Creating a demo for small scale automation.  This is a slack chatbot that watches a slack channel for commands, upon getting those commands it will exicute a function.  Currently it will do: 
  Some basic trouble shooting such as checking BPG neighbors, NTP sync status, CPU usage, and looks in the log for EIGRP, OSPF flaps, recursion, flapping mac addresses, and Duplicate addresses.
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
       find ip 172.16.1.250
       
       Device: Home_Switch
               interface Vlan2
               Device IP:  172.16.1.1
               Subnet Mask: 255.255.255.0
       ===========

