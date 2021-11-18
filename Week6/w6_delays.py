from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

my_device = {
    'host': "192.8.99.135",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_nxos',
    #delay can be global or on a command level (see output= below)
    'global_delay_factor': 2
}

net_conn = ConnectHandler(**my_device)
# delay_factor flag used here for the command copy run start
output = net_conn.send_command("copy run start", delay_factor=8)
#print(net_conn.find_prompt())
print(output)
net_conn.disconnect()