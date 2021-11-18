from netmiko import Netmiko
from getpass import getpass

# could also import the function such as
# from netmiko import ConnectHandler
# or
# from netmiko import ConnectHandler as ssh_tool
# where ssh_tool is a name you want to use later in the script to use that function

# getpass stops passwords being saved in files and prompting on screen.

## first method

''' one method for the connection
net_conn = Netmiko(host="192.40.228.37", username='bob',
                   password=getpass(), device_type='linux')
print(net_conn.find_prompt())
'''
## second method

'''
my_device = {
    'host': "192.40.228.37",
    'username': 'bob',
    'password': getpass(),
    'device_type': 'linux'
}

net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())
'''

# using with an enable secret
# if user password and enable secret is the same can use the below to ask for details just once:
# and reference the variable in the dictionary.
password = getpass()

my_device = {
    'host': "192.40.228.37",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'linux'
}

# send command only displays the output, not the prompt or the command it self
output = net_conn.send_command("show ip")
net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())
print(output)

# can change the pattern it searches for after a command is run with flag (using RegEx)
output = net_conn.send_command("show ip", expect_string=r'#')


''' more useful example:

my_device = {
    'host': "192.8.99.137",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_asa'
}

net_conn = ConnectHandler(**my_device)
output = net_conn.send_command("show ip")
output2 = net_conn.send_command("show arp")
print(net_conn.find_prompt())
print(output, output2)
output = net_conn.send_command("show run interface", expect_string=r'#')
'''

## If multiple devices

firewall1 = {
    'host': "192.8.99.137",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_asa'
}

firewall2 = {
    'host': "192.8.99.137",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_asa'
}

firewall3 = {
    'host': "192.8.99.137",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_asa'
}

for device in (firewall1, firewall2, firewall3):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show ip")
    print(output)

net_conn.disconnect()