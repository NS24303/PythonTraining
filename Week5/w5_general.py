
def which_dns():
    print("DNS Server 1 is: 8.8.8.8")
    print("DNS Server 2 is: 8.8.4.4")
#   return or return none is implied

which_dns()
which_dns()

# functions always have none type

return_val = which_dns()
print(return_val)
print(type(return_val))

print("-"*65)

def which_dns(dns):
    print("DNS Server is: {}".format(dns))
    return

which_dns("8.8.8.8")
which_dns("8.8.4.4")

print("-"*65)

def which_dns(dns, username, password):
    print("DNS Server is: {}".format(dns))
    print(username)
    print(password)
    return

which_dns("8.8.4.4", 'bob', 'password')
# the above is solely based on position, i.e. password being the 3rd entry
print("-"*65)
# named arguments are a better method:
which_dns(password='random', dns="1.1.1.1", username='jack')

print("-"*65)
# default values, here we have john as the default user
def which_dns(dns, password, username='john'):
    print("DNS Server is: {}".format(dns))
    print(username)
    print(password)
    return

which_dns(password='random', dns="1.1.1.1")

print("-"*65)

my_list = ['192.168.145.100', 'admin', 'password']

# the * is added to tell python to treat the 3 elements in the list as elements to pass in.
# without doing this it attempts to pass all 3 into dns entry.
which_dns(*my_list)

print("-"*65)

my_dict = {
    'dns': '172.16.78.3',
    'username': 'Jane',
    'password': 'something'
}
# with a dictionary we use **
which_dns(**my_dict)

print("-"*65)

dns_add2 = '1.1.1.1'

# python will first check for variables inside the the function, then use global values
def which_dns(dns, password='admin', username='john'):
    print("DNS Server is: {}".format(dns))
    print("DNS Server 2 is: {}".format(dns_add2))
    print(username)
    print(password)
    return

which_dns('8.8.8.8')