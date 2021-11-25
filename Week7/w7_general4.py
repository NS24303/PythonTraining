import jinja2

bgp_vars = {
    "routers": {
        'sf_rtr1': '10.10.10.1',
        'sf_rtr2': '10.10.10.2',
        'la_rtr1': '10.10.200.1',
        'denver_rtr1': '10.55.10.1',
    },

    "ip_list": [
        '192.168.100.1',
        '192.168.99.50',
        '172.16.20.30'
    ],

    "ipv6_enabled": True,
    "ipv4_enabled": True,
}

z_template = '''

{%- if ipv4_enabled %}
IPv4 is enabled
{%- if ipv6_enabled %}
IPv6 is enabled
{% endif %}
{% endif %}


{%- for router_name, ip_addr in routers.items() %}
{{router_name}} >>> {{ ip_addr }}
    {%- for ip_addr in ip_list %}
    {{ ip_addr }}
    {%- endfor %}
{%- endfor %}

{{ routers['sf_rtr1'] }}
{{ routers.sf_rtr2 }}


'''

template = jinja2.Template(z_template)
print(template.render(bgp_vars))
