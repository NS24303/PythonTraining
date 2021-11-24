# importing variables from csv

import jinja2
import csv

csv_file = "bgp_variables.csv"

with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for bgp_vars in read_csv:
        advertised_routes = bgp_vars['advertised_routes']
        advertised_routes = advertised_routes.split()
        #convert csv string to a list
        bgp_vars['advertised_routes'] = advertised_routes

        template_file = 'nxos_bgp2.j2'
        with open(template_file) as f:
            bgp_template = f.read()

        template = jinja2.Template(bgp_template)
        print()
        print('-'*65)
        print(template.render(bgp_vars))
        print('-' * 65)
