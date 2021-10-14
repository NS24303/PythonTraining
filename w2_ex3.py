'''Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline
character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".'''

from pprint import pprint


with open("show_arp.txt") as f:
    arp_table = f.readlines()

arp_table = arp_table[1:]
pprint(arp_table)

arp_table.sort()
arp3 = arp_table[:3]
print("\n\n" ,arp3)

## recreate as a table
arp3 = "\n".join(arp3)
print("\n\n" ,arp3)

# t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default.
# https://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes

f = open("arp_entries.txt", mode="w")
f.write(arp3)
f.flush()