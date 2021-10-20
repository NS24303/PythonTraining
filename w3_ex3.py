'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file.
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id".
Save these two items into variables and print them to the screen. You should extract only the
system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15').
Break out of your loop once you have retrieved these two items.
'''

with open("show_lldp_neighbors.txt") as f:
    show_lldp = f.read()

for line in show_lldp.splitlines():
    fields = line.split()
    if 'Port' in line:
        port_id = fields[2]
        continue
    elif 'System' in line:
        sys_id = fields[2]
        break

print(sys_id, port_id)