import sys
import netmiko
import re
from pprint import pprint

pprint(sys.path)


print("\n\nThe location (path) of RE is: \n")
print(re.__file__)
print("Version number is: ", re.__version__)
print("\n\nThe location (path) of Netmiko is: \n")
print(netmiko.__file__)
print("Version number is: ", netmiko.__version__)
# print(help(netmiko))
# print(help(re))