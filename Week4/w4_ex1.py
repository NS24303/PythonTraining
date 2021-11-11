'''
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper',
then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for
'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
'''

net_device = {}
bgp_fields = {}

net_device['ip_addr'] = '240.10.20.30'
net_device['vendor'] = 'Juniper'
net_device['username'] = 'random_user'
net_device['password'] = 'random_password'

bgp_fields['bgp_as'] = '1580'
bgp_fields['peer_as'] = '9857'
bgp_fields['peer_ip'] = '123.21.87.65'

print(net_device)
print(bgp_fields)

if 'Juniper' in net_device['vendor']:
    net_device['platform'] = 'Junos'

if 'Cisco' in net_device['vendor']:
    net_device['platform'] = 'ios'

print('=' *60)
net_device.update(bgp_fields)

print(net_device)

print('=' *60)

for key in net_device:
    print(key)

print('=' *60)

for key, value in net_device.items():
    print(key+':' , value)


''' 
could have ensured vendor was lower case, but chose not to. 

could have defined the dict in one for example
 
 bgp_fields = {
    "bgp_as": 42,
    "peer_as": 100,
    "peer_ip": "172.16.31.100",
}
'''