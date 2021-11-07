
# create a new dictionary variable
net_device = {}

print(type(net_device))

net_device['ip_addr'] = '192.168.1.99'
print(net_device)

var1 = 'Vendor'
net_device[var1] = 'Arista'
net_device['Device Type'] = 'EoS'
print(net_device)

# do not count on the order of a dictionary unless using ordered dictionary.
print(net_device['Device Type'])
print(net_device['Vendor'])

# change the value of a entry
net_device['Vendor'] = 'Dell'
print(net_device['Vendor'])

# graceful way of handling execptions is using try/accept statment (covered later)
# another way is using .get method

print(net_device.get('model'))
# or to print an error message
print(net_device.get('model', 'Does not Exist'))

# remove a key from dictionary
print(net_device)
net_device.pop('Vendor')
print(net_device)


net_device2 = {'Model': '7050'}
net_device.update(net_device2)
print(net_device)
# can use this to update/overwrite values in original dictionary

# print key
print("--- Keys ---")
for key in net_device:
    print(key)

# print value
print("--- Value using value method ---")
for value in net_device.values():
    print(value)

# print key and value
print("--- Key and Value using Item method ---")
for value in net_device.items():
    print(value)

# print key and value
print("--- Key and Value enumerate ---")
for key, value in net_device.items():
    print(key)
    print(value)

# Sets
# note duplicate is there on purpose to demo that Sets ignore duplicates
ipam = {'1.1.1.1', '8.8.8.8', '8.8.4.4', '1.0.0.1', '1.1.1.2', '1.1.1.1'}
ipam_two = {'149.112.112.112', '9.9.9.9', '208.67.222.222', '208.67.220.220', '1.1.1.2', '1.1.1.1'}
#print(type(ipam), type(ipam_two))
print("set one is:" ,ipam)
print("set two is:" ,ipam_two)

# union - unique elements in both sets, no duplicates
print("union of sets is \n" ,ipam | ipam_two ,"\n")
# another method to do the union
# print(ipam.union(ipam_two))

# intersection of the two sets - only common elements
print("intersection of sets is \n" ,ipam & ipam_two,"\n")
# another way to do the intersection
# print(ipam.intersection(ipam_two))

# remove anything that is common from ipam_two which is also in ipam
print("difference of sets is \n",ipam_two - ipam,"\n")
# another way to do this
#print(ipam_two.difference(ipam))

# symmetric difference - xor - only unique elements in the two sets
print("symmetric difference of sets is \n" ,ipam_two ^ ipam,"\n")
# another way to do this
#print(ipam.symmetric_difference(ipam_two))

# exceptions
my_dict = {}
# below line will produce error on purpose to give example (if not commented out)
# my_dict['ip_addr']
# this error will exit the script

# this try function handels the error gracefully
# rather than exiting the script it will print out the error message in KeyError.
'''
try:
    print("this is before")
    my_dict['ip_addr']
    print("this is after")
except KeyError:
    print("Found an Error")
# can also re-raise the error message, but it also exits script
    raise
'''

# alternative method
try:
    my_dict['ip_addr']
except KeyError as e:
    print(e.__class__)
    print(str(e))
    print("found an error, printed info above")

# catch multiple exceptions
my_list = []
try:
    my_dict['ip_addr']
    my_list[0]
except (KeyError, IndexError):
    print("handled two errors")
# could have 2 except lines, one for each type of error with different actions, i.e. prints
finally:
# happens regardless of an exception being found or not
    print("finally, always executed")
# Note KeyError = dictionary
# whereas IndexError = lists

# could handle any exception, regardless of type with
#   except Exception
#   print("any exception")

print("script ended gracefully")

