'''
*** Note, to actually test this in your environment, change the test IP addresses to
something in your environment that you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index.
The output should look similar to the following:
0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list.
For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs.
This should be similar to the following:

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
'''

import os

subnet = '10.10.100.'

WINDOWS = False

base_cmd_linux = "ping -c 2"
base_cmd_windows = "ping -n 2"
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

## my attempt so far

ip_range = []
for i, octet in enumerate(range(1, 255)):
    ip_addr = subnet + str(octet)
    ip_range.append(ip_addr)

# one way to do the following - using a while loop - this works for print
# Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.
  
    while i >= 2 and i <= 5:
        print(i, "--->", ip_addr)
        break

#however
ip_range = ip_range[2:6]
print('-' * 40)
print(ip_range)
print(base_cmd)

for ip in ip_range:
    print("IP Address to ping is: ", ip)
    return_code = os.system("{} {}".format(base_cmd, ip))
    print("-" * 80)
print()

'''
attempted to use join rather then + but didnt get this working
'''