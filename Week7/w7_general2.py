# Jinja2 - take a list of variables and a configuration template and output a bunch of files
# could be used to produce a base configuration for many devices.

# importing template configuration from file

import jinja2

bgp_vars = {
    "peer1_ip": "192.168.100.10",
    "peer1_as": 30,
    "advertised_route1": "10.10.10.0/24",
    "advertised_route2": "10.10.30.0/24",
    "advertised_route3": "10.10.40.0/24",
}

template_file= 'nxos_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_vars))

print('='*65)

# The same again except with a loop for advertised routes
# this uses a for loop in the template_file nxos_bgp2.j2

advertised_routes =["192.168.100.0/24", "192.168.40.0/24", "192.168.60.0/24"]

bgp_var_v2 = {
    "peer1_ip": "192.168.100.10",
    "peer1_as": 30,
    "advertised_routes": advertised_routes,
}

template_file2= 'nxos_bgp2.j2'
with open(template_file2) as f:
    bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_var_v2))


print('='*65)

# The next example uses a conditional

advertised_routes =["192.168.100.0/24", "192.168.40.0/24", "192.168.60.0/24"]

bgp_var_v3 = {
    "peer1_ip": "192.168.100.10",
    "peer1_as": 30,
    # template uses ipv6 address family only if below is true
    "peer1_ipv6": True,
    "advertised_routes": advertised_routes,
}

template_file3= 'nxos_bgp3.j2'
with open(template_file3) as f:
    bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_var_v3))