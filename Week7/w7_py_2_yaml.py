import yaml


my_dict = {
    'rtr11': {'bgp_peers': ['1.1.1.1', '2.2.2.2', '3.4.4.4'],
              'device_type': 'cisco_ios',
              'ip_addr': '10.85.32.24',
              'password': 'whatever',
              'username': 'admin'},
    'rtr12': {'bgp_peers': ['1.1.10.1', '25.54.25.45', '161.65.58.33'],
              'device_type': 'cisco_nxos',
              'ip_addr': '10.95.32.24',
              'password': 'whatever',
              'username': 'admin'},
    'rtr13': {'ip_addr': '23.54.34.123'},

}

print(my_dict)
filename = "yaml_output.yml"
with open(filename, "w") as f:
    # flow style defines how the output yaml is formatted, either expanded or compressed
    output = yaml.dump(my_dict, f, default_flow_style=False)
    #output = yaml.dump(my_dict, f)

'''
 when set to true output looks like

{rtr11: {bgp_peers: [1.1.1.1, 2.2.2.2, 3.4.4.4], device_type: cisco_ios, ip_addr: 10.85.32.24,
    password: whatever, username: admin}, rtr12: {bgp_peers: [1.1.10.1, 25.54.25.45,
      161.65.58.33], device_type: cisco_nxos, ip_addr: 10.95.32.24, password: whatever,
    username: admin}, rtr13: {ip_addr: 23.54.34.123}}

'''

''' 

when set to false

rtr11:
  bgp_peers:
  - 1.1.1.1
  - 2.2.2.2
  - 3.4.4.4
  device_type: cisco_ios
  ip_addr: 10.85.32.24
  password: whatever
  username: admin
rtr12:
  bgp_peers:
  - 1.1.10.1
  - 25.54.25.45
  - 161.65.58.33
  device_type: cisco_nxos
  ip_addr: 10.95.32.24
  password: whatever
  username: admin
rtr13:
  ip_addr: 23.54.34.123

'''

