'''Create a list of five IP addresses. use the .append() method to add an IP address onto the end of the list.
Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list.
Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.'''

ipam = ['172.16.10.10', '172.16.20.20', '172.16.30.30', '172.16.40.40', '172.16.50.50']

print("The variable ipam is of type" ,type(ipam))
print("ipam currently holds" ,len(ipam) ,"ip Addressess")
print("The current contents of the list are\n" ,ipam)

ipam.append('172.16.60.60')
print("adding one IP using append. The ipam now holds" ,len(ipam) ,"ip Addressess")

ipam.extend(['172.16.70.70', '172.16.80.80'])
print("adding two IP using extend. The ipam now holds" ,len(ipam) ,"ip Addressess")

# remember that concatenation does not modify the orignal list, it creates a new list.
# to do this we need to redefine the variable
ipam = ipam + ['172.16.90.90', '172.16.100.100']
print("adding two IP using concatenation. The ipam now holds" ,len(ipam) ,"ip Addressess")
print("The current contents of the list are\n" ,ipam)

print("The first IP in the ipam is: " ,ipam[0])
print("The last IP in the ipam is: " ,ipam[7])

ipam.pop(0)
print("Popping zero. The ipam now holds" ,len(ipam) ,"ip Addressess")
print("The current contents of the list are\n" ,ipam)
ipam.pop(8)
print("Popping nine. The ipam now holds" ,len(ipam) ,"ip Addressess")
print("The current contents of the list are\n" ,ipam)

ipam[0] ='2.2.2.2'
print("The current contents of the list are\n" ,ipam)