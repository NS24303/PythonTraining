'''Read in the "show_ip_int_brief.txt" file into your program using
the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface.
You can just hard-code the index at this point since
we haven't covered for-loops or regular expressions.

Use the string .split() method to obtain both the IP address and the
corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero.
You might need to 'pip install pycodestyle' on your
computer (you should be able to type this from the shell prompt).
Alternatively, you can type 'python -m pip install pycodestyle'.'''

with open("show_ip_int_brief.txt") as f:
    ip_int_br = f.readlines()

# print(ip_int_br)

# grab the Ethernet4 line
fast4 = ip_int_br[5]
print("\n\n", fast4)

# split this list and grab interface name and ip only
fast4 = fast4.split()
int = fast4[0]
ip = fast4[1]

print(int, ip)

the_tuple = (int, ip)
# print(type(the_tuple))
print(the_tuple)

# syntax for using pycodestyle is:
# pycodestyle <script_name>
