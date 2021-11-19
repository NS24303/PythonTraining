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


''' output from live devices:
=============== BEFORE using textFSM 

bash-4.2# python3 test_textfsm.py
Password:
	NeverNetworks_admin 192.168.99.129 fc99.4749.b0b2 725
	NeverNetworks_admin 192.168.99.131 c464.1336.f741 785
	NeverNetworks_admin 192.168.99.130 fc99.4749.ae5e 2991
	Failover 10.24.63.26 cc16.7e91.884d 1370
<class 'str'>

=============== WITH using textFSM 

bash-4.2# vim test_textfsm.py
bash-4.2# python3 test_textfsm.py
Password:
[{'interface': 'NeverNetworks_admin', 'address': '192.168.99.129', 'age': '782', 'mac': 'fc99.4749.b0b2'}, {'interface': 'NeverNetworks_admin', 'address': '192.168.99.131', 'age': '842', 'mac': 'c464.1336.f741'}, {'interface': 'NeverNetworks_admin', 'address': '192.168.99.130', 'age': '3048', 'mac': 'fc99.4749.ae5e'}, {'interface': 'Failover', 'address': '10.24.63.26', 'age': '1427', 'mac': 'cc16.7e91.884d'}]
<class 'list'>'''

