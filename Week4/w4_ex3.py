'''
Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version,
serial number, and configuration register values.

Your output should look as follows:

OS Version: 15.4(2)T1
Serial Number: FTX0000038X
Config Register: 0x2102
'''
import re

with open("show_version.txt") as f:
    show_ver = f.read()

print("Config Register: ")

#
# short version, stopping at ,
print("OS Version:" ,re.search(r"Version (.*),", show_ver, flags=re.M).group(1))
# full version, going to end of line
print("OS Version:" ,re.search(r"Version (.*)$", show_ver, flags=re.M).group(1))
print("Serial Number:" ,re.search(r"ID (.*)$", show_ver, flags=re.M).group(1))
print("Config Register:" ,re.search(r"register is (.*)$", show_ver, flags=re.M).group(1))