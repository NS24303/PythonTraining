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
# Ternary operator - conditional expressions which uses boolean to confirm if a condition is true or not.
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_range = []
for i, octet in enumerate(range(1, 255)):
    ip_addr = subnet + str(octet)
    # ip_addr is a string so we append it to the list ip_range
    ip_range.append(ip_addr)

# I used a while loop to get ips .3 -> 6 which I initially printed to screen
# but on further thought I saved to a new variable

    while i >= 2 and i <= 5:
        #print(i, "--->", ip_addr)
        short_list = (i, "--->", ip_addr)
        # this actually created a tuple rather than list
        #print(short_list)
        just_ip = short_list[2]
        print("IP Address to ping is:" ,just_ip)
        return_code = os.system("{} {}".format(base_cmd, just_ip))
        print("-" * 40 ,"\n")
        break

'''
# an alternative approach based on the answer
ip_range = ip_range[2:6]
print('-' * 40)
print(ip_range)

for ip in ip_range:
    print("IP Address to ping is: ", ip)
    return_code = os.system("{} {}".format(base_cmd, ip))
    print("-" * 80)
print()
'''
