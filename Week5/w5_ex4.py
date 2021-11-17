'''
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside
of your function (i.e. where you have your function calls).

Inside of pdb, experiment with:
Listing your code.
Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
Experiment with 'up' and 'down' to move up and down the code stack.
Use p <variable> to inspect a variable.
Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = [])
'''

# not much to see here other than a breakpoint

import re
import pdb

def mac_format(mac_address):
    mac_address = mac_address.upper()
    if ":" in mac_address or "-" in mac_address:
        new_mac = []
        octets = re.split(r"[-:]", mac_address)
        # print(octets)
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif "." in mac_address:
        new_mac = []
        sections = mac_address.split(".")
        # print(sections)
        # i created this additional if statement for a use case where a mac address is xx.xx.xx.xx.xx.
        # this may never be required but wanted to try it.
        if len(sections) == 6:
            print(":".join(sections))
        if len(sections) == 3:
            for word in sections:
                if len(word) < 4:
                    word = word.zfill(4)
                new_mac.append(word[:2])
                new_mac.append(word[2:])

    return ":".join(new_mac)


pdb.set_trace()
print(mac_format('a:b:c:d:e:f'))
print(mac_format('fc:99:47:49:b0:b1'))
print(mac_format('001c.c4bf.826a'))
print(mac_format('ee.97.37.29.a1.c3'))