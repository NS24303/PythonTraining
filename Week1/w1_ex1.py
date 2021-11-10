''' Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three
corresponding IP addresses). Print these three variables to standard output using a single print statement.
Make your print statement compatible with both Python2 and Python3.'''

ip_a = '1.1.1.1'
ip_b = '8.8.8.8'
ip_c = '8.8.4.4'

import sys
print("Python Version is\n",sys.version ,"\n\n")

# If wanting to keep simple while ensuring works with python2 or 3:
# from __future__ import print_function
# print (ip_a, ip_b, ip_c)

print("{:^15}{:^15}{:^15}".format(ip_a, ip_b, ip_c))

#first try python2 method
#try:
#    ip_addr2 = raw_input("Enter another IP Address: ")
    # Then try Python3 method
#except NameError:
#    ip_addr2 = input("Enter Another IP Address:")