''' Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain
the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.'''

from num2words import num2words

with open("show_ip_bgp_summ.txt") as f:
    output = f.readlines()

line0 = output[0]
line1 = output[1]
line21 = output[21]

line1_list = line1.split()
local_as = line1_list[7]
local_ip = line1_list[3]

line0_list = line0.split()
hostname = line0_list[0]

line21_list = line21.split()
remote_as = line21_list[2]
remote_ip = line21_list[0]
uptime = line21_list[8]
prefixes = line21_list[9]

# using rstrip here to remove the comma ',' from the IP address output
local_ip = local_ip.rstrip(',')
# using rstrip here to remove the comma '#' from the hostname
hostname = hostname.rstrip('#')

print("The hostname of the router is: " ,hostname)
print("The Local IP Address for your BGP output is: " ,local_ip)
print("The Local AS Number for your BGP output is: " ,local_as)

print("The remote AS Number for your BGP output is: " ,remote_as)
print("The remote Peer IP address for your BGP output is: " ,remote_ip)
print("The Peering has been up for: " ,uptime)
print("The amount of learnt prefixes is: " ,prefixes)

# Below is just something I wanted to see if it was possible, it has no real value
# but it convers the number of prefixes to words.
print(num2words(prefixes))

# note this is very basic as it currently stands as it assumes output is on a given line
# in future I would like to adapt this to automatically loop through and find all the peer IPs






