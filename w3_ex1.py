'''
Read the "show_vlan.txt" file into your program.
Loop through the lines in this file and extract all of the VLAN_ID,
VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a
 new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME).
 Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
 '''

from pprint import pprint

with open("show_vlan.txt") as f:
    show_vlan = f.readlines()

pprint(show_vlan[2:])

'''
Need to change this for a for loop rather than while. 

show_vlan = open("show_vlan.txt")
i = 2

while i <=5:
    output = show_vlan.readline()
    vlan = output[0]
    name = output[1]
    print("\n", vlan, name)
    i += 1
'''