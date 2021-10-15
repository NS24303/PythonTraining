''' Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain
the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.'''

with open("show_ip_bgp_summ.txt") as f:
    output = f.readlines()


line1 = output[1]
line21 = output[21]

line1_list = line1.split()
local_as = line1_list[7]
local_ip = line1_list[3]
local_ip = local_ip.rstrip(',')


print(line1)
print(line21)

print("The Local IP Address for your BGP output is: " ,local_ip)
print("The Local AS Number for your BGP output is: " ,local_as)

