'''
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''
import re

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

print(mac_format('a:b:c:d:e:f'))
print(mac_format('fc:99:47:49:b0:b1'))
print(mac_format('001c.c4bf.826a'))
print(mac_format('ee.97.37.29.a1.c3'))


''' 
The below code was my original attempt at this exercise. 
This worked for the general formatting but did not perform any padding in the case of a:b:c:d:e:f

def mac_format(mac_addr):
    mac_addr = mac_addr.upper()
    mac_addr = mac_addr.replace(".", "")
    mac_addr = mac_addr.replace(":", "")
    while len(mac_addr) > 0:
        entry = mac_addr[:2]
        mac_addr = mac_addr[2:]
        new_mac.append(entry)
    new_mac = ":".join(new_mac)
    return new_mac
    
# zfill is used to fill a string with zeros until it is a certain length in size (x)
'''
