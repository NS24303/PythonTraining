
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