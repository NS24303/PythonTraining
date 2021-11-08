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

print(re.search(r".", ip_add))

# .group is used to confirm what matched
# remember . in regex is any charater
print(re.search(r"....", ip_add).group(0))

# + match any character any ammount of times
print(re.search(r".+", ip_add).group(0))

# * match any character any character zero or more times
print(re.search(r".*", ""))

print(re.search(r"^\d+", ip_add))

