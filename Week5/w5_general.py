import pdb

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

# insert a debugging breakpoint
# pdb.set_trace()
# commands:
# list . (shows what line we are on script
# list 1, 20 ( shows line 1-> 20)
# s (step through the program line by line)
# args (list the arguments)
# p <variable> (print variable)
# up (previous line in script)
# down (next line in script)
# n goes to next section in script within the same level
# return (continues to return line of a function)
# can also be run with:
# python -m pdb <script_name.py>
# by doing this you dont need to import and have a breakpoint
# b 10 (breakpoint at line 10)
# continue (keep going until hits breakpoint)
# !<python_code> (run some other code in the debugger

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

print("-"*65)

# classes let you pass around variables between functions

# in python2 you would do class MyClass(object):
# classes use SentanceCase (no underscores)
# https://www.w3schools.com/python/python_classes.asp

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("-"*65)

# importing of modules and functions.
# python packages
# List comprehension - convert a list to different form

my_list = [1,2,3,4,5]
print(my_list)
my_list2 = [x**2 for x in my_list]
print(my_list2)

# lambda functions (1 line disposable function)

f = lambda x: x**2
print(f(10))
