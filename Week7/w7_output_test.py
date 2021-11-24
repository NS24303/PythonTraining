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

        template_file = 'nxos_bgp_output.j2'
        with open(template_file) as f:
            bgp_template = f.read()

        template = jinja2.Template(bgp_template)
        hostname = bgp_vars['device_id']
        print()
        print('-'*65)
        print(template.render(bgp_vars))
        print('-' * 65)
        # attempting to write the configuration to files.
        # target is 1 file per line in the CSV
        f = open(hostname + ".txt",  mode="w")
        f.write(template.render(bgp_vars))
        f.flush()


    ''' Attempt 1 to define a file_name
        filename = "bgp_config"
        i = 1
        i = str(i)
        output_file= filename + i + ".txt"
        print(output_file)
        i = int(i)
        i = i + 1
        
        this created the filename correctly, but did not increment,
        rather than this I added a new column to the csv for device_id 
        and used this in the above
     '''