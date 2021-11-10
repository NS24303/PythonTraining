''' recap of RegEx special charaters
.       any single character
+       one or more times
*       zero or more times
^       beginning of line
$       end of line
\s      whitespace character class
\d      digit character class
\S      non-whitespace character class
[]      define own character class
()      save things'''

# re is used to search
import re

ip_add = "10.23.100.240"

print(re.search(r"..", ip_add))

# .group is used to confirm what matched
# remember . in regex is any charater
print(re.search(r"....", ip_add).group(0))

# + match any character any ammount of times
print(re.search(r".+", ip_add).group(0))

# * match any character any character zero or more times
print(re.search(r".*", ""))

print(re.search(r"^\d+", ip_add))


with open("show_version.txt") as f:
    output = f.read()

show_ver = output.splitlines()
line = show_ver[0]

# group(0) is used to show the entire line that is matched
# print(re.search(r"^C.*$", line).group(0))

# match just the software version element
print(re.search(r"^C.*, Version (\S+),.*$", line).group(1))
# match the device type (could be done in same line as above)
device_type = re.search(r"Software, (\S+).*$", line).group(1)
print(device_type)

# name a saved regex capture using ?P<serial_num>
print(re.search(r"^C.*, Version (?P<version>\S+),.*$", line).groupdict())

# by default .* will grab as much as it can, this means it wont stop on the first , but the last
print(re.search(r"^Cisco (.*), ", line).group(1))
#  we can stop this with the ? after the .* (also called non-greedy)
print(re.search(r"^Cisco (.*?), ", line).group(1))

# below would not work as ^ is begging of string, not line. This would match Cisco at start of show version
# print(re.search(r"^Processor board ID (.*)$", output).group(0))
# need to match on every line we can use the multiline flag re.M
print(re.search(r"^Processor board ID (.*)$", output, flags=re.M).group(1))



# this will not match the whole of output, .* does not match new lines
print(re.search(r"^Cisco.*", output).group(0))
# to change this use DOTALL flag
print(re.search(r"^Cisco.*", output, flags=re.DOTALL).group(0))
# i flag is ignore case in regex
print(re.search(r"^Cisco.*", output, flags=re.I).group(0))