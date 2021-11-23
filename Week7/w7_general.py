# Jinja2 - take a list of variables and a configuration template and output a bunch of files
# could be used to produce a base configuration for many devices.

import jinja2

bgp_vars = {
    "peer1_ip": "192.168.100.10",
    "peer1_as": 30,
    "advertised_route1": "10.10.10.0/24",
    "advertised_route2": "10.10.30.0/24",
    "advertised_route3": "10.10.40.0/24",
}

bgp_template = '''
feature bgp
router bgp 10
  address-family ipv4 unicast
    network {{ advertised_route1 }}
    network {{ advertised_route2 }}
    network {{ advertised_route3 }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback0 
    ebgp-multihop2
    address-family ipv4 unicast
'''

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))


