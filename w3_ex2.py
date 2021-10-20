'''
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file.
Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you
have found both of these devices, 'break' out of the for loop.
'''

arp_table = []
with open("show_arp.txt") as f:
    show_arp = f.read()

for line in show_arp.splitlines():
    if "Protocol" in line:
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if '10.220.88.1' in line:
        print("Default gateway IP/Mac: ")
        print(ip_addr)
        print(mac_addr)
#        continue
    if '10.220.88.30' in line:
        print("Arista3 IP/Mac is: ")
        print(ip_addr)
        print(mac_addr)
        break
'''
Line 20: Could have used line.lower() to ignore case of protocol
Line 29: continue is not required here. 
line 30: should have used elif rather than if. But both work. -
using another if like I did is like a seperate function/section. 
Where as using elif would have continued the previous if function. 

line 26 & 31: alernative method for formatting:
print("Default gateway IP/Mac is: {}/{}".format(ip_addr, mac_addr))
^ this looks nicer but no real difference. Good to know

General: Accepted answer was to use boolean to change to true when the 
two IP/MAC addresses are found. Then use an if statement to end when both are true.

I used a general break once it found the second without boolean
'''