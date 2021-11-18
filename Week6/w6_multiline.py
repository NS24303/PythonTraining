from netmiko import Netmiko
from getpass import getpass

# script for working a command which sends back something other than the prompt
# in this case, deleting a file which will ask user to confirm

password = getpass()
filename ="asa983-26-smp-k8.bin"

firewall3 = {
    'host': "192.8.99.137",
    'username': 'bob',
    'password': password,
    'secret': password,
    'device_type': 'cisco_asa'
}

# one solution to the wait is send cmd timing:
# output = net_connect.send_command_timing(cmd)
# standard timeout is 100 seconds for send command

net_connect = Netmiko(**firewall3)
cmd = "delete flash:{}".format(filename)

output = net_connect.send_command_timing(
    command_string=cmd,
    strip_prompt=False,
    strip_command=False
)

if 'delete' in output:
    output = net_connect.send_command_timing("\n")

if 'confirm' in output:
    output = net_connect.send_command_timing("\n")

net_connect.disconnect()
print(output)


