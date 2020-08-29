from functions import *
from pprint import pprint

network_setup_file = 'org.yml'

network_setup = read_in_yaml_file(network_setup_file)

def pull_cpu_usage(ssh_connection):
    command = 'show processes cpu sorted'
    output = send_command(ssh_connection,command)
    output = make_output_list(output)
    for line in output:
        if 'CPU utilization for' in line:
            cpu_use = line.split(';')[-1]
            cpu_use = int(cpu_use.split(' ')[-1][:-1])

    return cpu_use


def make_output_list(output):
    return_this = []
    output = output.split('\n')
    return output

def check_ntp_synch(ssh_connection):
    bad_indicators = ['unsynchronized', 'NTP is not enabled']
    command = 'show ntp status'
    output = send_command(ssh_connection,command)
    for item in bad_indicators:
        if item in output:
            return False
    return True

def sort_log(ssh_connection):
    bad_indicators = ['DUAL', 'OSPF', 'recursion', 'BGP', 'flapping between port',
    'Duplicate address', 'MACFLAP', ]
    command = 'show log'
    output = send_command(ssh_connection,command)
    output = make_output_list(output)
    bad_lines = []
    for line in output:
        for indicator in bad_indicators:
            if indicator in line:
                bad_lines.append(line)
    return bad_lines

def trouble_shoot_device(ip, username, password):
    output = {}
    ssh_connection = make_connection(ip, username, password)
    output['cpu_usage_percent'] = pull_cpu_usage(ssh_connection)
    output['ntp_working'] = check_ntp_synch(ssh_connection)
    output['questionable_log_lines']=sort_log(ssh_connection)
    pprint (output)


username = 'dhimes'
password = 'password'

for ip in network_setup['dc1']['devices']:
    trouble_shoot_device(ip, username, password)
