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