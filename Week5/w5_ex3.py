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

def mac_format(mac_addr):
    mac_addr = mac_addr.upper()
    mac_addr = mac_addr.replace(".", "")
    mac_addr = mac_addr.replace(":", "")
    new_mac = []
    while len(mac_addr) > 0:
        entry = mac_addr[:2]
        mac_addr = mac_addr[2:]
        new_mac.append(entry)
    new_mac = ":".join(new_mac)
    return new_mac

print(mac_format('001c.c4bf.826a'))

# above works for the formatting of a mac address in either 00:1c:c4 format, or 00.1c.c4 or 001c.c4
# need to spend time on this to figure out padding of a mac to 2 digits