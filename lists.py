
#list can contain multiple types of data
a_list = ['ip addresses', 30, 30]
print(type(a_list))

#print a single element from the list
print(a_list[1])

#change a value of one element from the list
a_list[1] = '100'
print(a_list[1])
print(len(a_list))

#append to a list
a_list.append(99)
print(len(a_list))

#add elemnets to a list:
a_list.extend([78, 23])
print(len(a_list))

#find entry in a list
print("100 is at index " ,a_list.index('100'))

#remove a specific entry in the list
a_list.remove('ip addresses')

#remove the last entry in a list
a_list.pop()
print(len(a_list))

#can also remove specific element from list
a_list.pop(0)
print(len(a_list))

### List slices
print("Now we look at list slices")
f =open("Week2/show_version.txt")
output = f.readlines()
print("The amount of lines in the list is" ,len(output) ,"and the type is" ,type(output) ,"\n")

#output lines 0 to 4
print(output[0:5])
# can ignore first number and just to
# [:5]
# or
# [:] will display all lines
# can also use minus numbers [-1:-5]
# this can be used to create a new list from another list

# A tuple is a list which you can not modify,
# can not change an element, extend etc

a_tuple = (1,2,3,4,54,65)
print (type(a_tuple))

# only way around this would be to convert type

the_new_list = list(a_tuple)
print (type(the_new_list))

#
ipv6_addr = "2001:0000:3238:DFE1:63:0000:0000:FEFB"
print(ipv6_addr.split(":"))
octets = ipv6_addr.split(":")
print(type(octets))

# join is re-adding the : to the IPv6 octets which form the list.
print(":".join(octets))

# importing a module. This module detects command line arguments
import sys
print(sys.argv)
# useful for importing command line arguments into a list to be used later?
