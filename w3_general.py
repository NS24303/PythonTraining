variable1 = 100

if variable1 == 200:
    print("variable 1 does not equal 100")
elif variable1 == 100:
    print("Variable1 equal to 100")
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

ip_table = ['10.10.10.10','20.20.20.20','30.30.30.30','40.40.40.40']


for ip_addr in ip_table:
    print("The IP address is:", ip_addr)

# enumerate option provides index of each entry in list.
# break exits the loop
for ip_addr in enumerate(ip_table):
    print("The IP address is:", ip_addr)
    #break

for i, ip_addr in enumerate(ip_table):
    print("index is", i)
    print("The IP address is:", ip_addr)
    print("-" * 20)

# break when ip_add is 20.20.20.20
print("=" * 80)

for ip_addr in ip_table:
    print("The IP address is:", ip_addr)
    if ip_addr == '20.20.20.20':
        break

print("=" * 80)

# continue statement here means when ip_addr is 20.20.20.20 skip and continue loop
for ip_addr in ip_table:
    print("hello")
    if ip_addr == '20.20.20.20':
        continue
    print("The IP address is:", ip_addr)

print("=" * 80)

ip_table2 = ['50.50.50.50','60.60.60.60']

# nested loops
for ip_addr in ip_table:
    for ip_addr2 in ip_table2:
        print(ip_addr)
        print(ip_addr2)

print("=" * 80)

#range commands
# casting range as a list:
print(list(range(5)))

# start the range at 4
print(list(range(4,9)))

# in the form of a loop, 2 options:
x = range(7)

for n in x:
    print("the range is" ,n)

for a_range in range(10):
    print(a_range)

print("=" * 80)

f = open("show_version.txt")
i = 0

# this will print 6 lines as i = 0 and loop is less than or equal to
while i <=5:
    print("LINE:::")
    print(f.readline())
    i += 1
    # another way to do the increment is i = i +_1

print("=" * 80)
i = 0

while i <=3:
    line = f.readline()
    line = line.strip()
    print("LINE:::" ,line)
    i = i + 1

print("=" * 80)

for ip_addr in ip_table:
    print("The IP address is:", ip_addr)
    if ip_addr == '20.99.20.20':
        break
else:
    print("you have hit the break clause")

print("=" * 80)

t = 100

# while true can be used to stops loops
while True:
    print("hello")
    print("hello")
    if t == 100:
        break
