'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file.
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id".
Save these two items into variables and print them to the screen. You should extract only the
system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15').
Break out of your loop once you have retrieved these two items.
'''

with open("show_lldp_neighbors.txt") as f:
    show_lldp = f.read()

# my approach below

for line in show_lldp.splitlines():
    fields = line.split()
    if 'Port' in line:
        port_id = fields[2]
        continue
    elif 'System' in line:
        sys_id = fields[2]
        break

print(sys_id, port_id)
print("Port ID: {}".format(port_id))

'''
Accepted answer again used boolean for the breaking out of script when the two variables were true
It also used the format method for the print statement. I used this as an example in line 24 to highlight the usage
The code below highlights the accepted answer. Note the _, this seems to take the text after system name or pord id
and store it in the variable 

system_name, port_id = (None, None)
for line in show_lldp.splitlines():
    if "System Name: " in line:
        _, sys_id = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")

    if port_id and system_name:
        break
        
print("System Name: {}".format(system_name))
print("Port ID: {}".format(port_id))
'''
