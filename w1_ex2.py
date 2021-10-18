'''
Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets.
Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

$ python exercise2.py
Please enter an IP address: 80.98.100.240
    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------
Four columns, fifteen characters wide, a header column, data centered in the column.
'''
#!/usr/bin/env python3

#first try python2 method
#try:
#    ip_addr2 = raw_input("Enter another IP Address: ")
    # Then try Python3 method
#except NameError:
#    ip_addr2 = input("Enter Another IP Address:")


ip_address = input ("Please enter an IP address: ")

octets = ip_address.split(".")
print("-"*80)
print("{:^15}{:^15}{:^15}{:^15}".format("octet1", "octet2", "octet3", "octet4"))
print("-"*80)
print("Dec{:^15}{:^15}{:^15}{:^15}".format(octets[0], octets[1], octets[2], octets[3]))
print("Bin{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print(
    "hex{:^15}{:^15}{:^15}{:^15}".format
    (hex(int(octets[0])),
     hex(int(octets[1])),
     hex(int(octets[2])),
     hex(int(octets[3]))
     )
)