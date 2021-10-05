x  = 10
y = 50
z = 1.05

T =  True
F = False

welcome = "welcome world"

print ("hello world")
print (welcome)

# print the value of x
print ("-- The value of the variable x is: ",(x))
#print the type of variable that x is
print ("-- The variable type of x is", (type(x)),'\n')

print ("-- The value of the variable z is: ",(z))
print ("-- The variable type of z is", (type(z)),'\n')

print ("-- The value of the variable welcome is: ",(welcome))
print ("-- The variable type of welcome is", (type(welcome)),'\n')

print ("-- The value of the variable T is: ",(T))
print ("-- The variable type of T is", (type(T)),'\n')

#multiple x by y
print ("Lets try some math! x=",(x), "and y=",(y))
print ("So if we multiple the two we get" ,(x*y),'\n')

#convert a variable from one to other - Called Casting
print ("Remember the current type of x is" ,type(x),"and the value is",(x))
print ("lets convert it to a float")
xfloat = float(x)
print ("the type of x is now",(type(xfloat)), "and the value of x is",(xfloat),'\n\n')

#multiply an string with a int

print ("this next part has no purpose other than to demo what python will do when you multiply and Int with a String")
answer = input ("type a word: ")
print (answer*x)
