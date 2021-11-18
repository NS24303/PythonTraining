from netmiko import Netmiko
from getpass import getpass

# script for working a command which sends back something other than the prompt
# in this case, deleting a file which will ask user to confirm
# https://vimeo.com/254611876?__s=vj5wphj66d6bujp5sehs
password = getpass()

my_device = {
    'host': "192.40.228.37",
    'username': 'bob',
    'password': password,
    'device_type': 'linux'
}

net_conn = Netmiko(**my_device)
output = net_conn.send_command("arp -a", use_textfsm=True)
print(output)
print(type(output))
net_conn.disconnect()
