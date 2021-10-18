variable1 = 100

if variable1 == 200:
    print("variable 1 does not equal 100")
elif variable1 == 100:
    print ("Variable1 equal to 100")
else:
    print("Variable1 is equal to something else")

# ternary operator
my_val = 10
a = 'Greater_then_2' if my_val > 2 else 'Less_then_2'
print(a)

# None is its own datatype in Python. It is always false
# it is the default return value from all functions if not using anything else.
T = None
print(type(T))

ip_table = ['10.10.10.10', '20.20.20.20', '30.30.30.30', '40.40.40.40']


for ip_addr in ip_table:
    print("The IP address is:" ,ip_addr)

# enumerate option provides index of each entry in list.
# break stops the loop
for ip_addr in enumerate(ip_table):
    print("The IP address is:" ,ip_addr)
    #break

for i, ip_addr in enumerate(ip_table):
    print("index is" ,i)
    print("The IP address is:" ,ip_addr)
    print("-" * 20)
