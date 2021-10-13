''' Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents
to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a
string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using
the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable
(you should have a list at this point).
'''

print("\n\n ....Reading show_version.txt into a variable called output.... \n")

# first method (prefered). This is the method with a context manager
with open("show_version.txt") as f:
    output2 = f.readlines()


#alternative method is
f = open("show_version.txt")
output = f.read()

print("The type of variable for regular output is"  ,type(output) ,"\n\n")
print("The type of variable for context manager output is"  ,type(output2) ,"\n\n")
print (output)
print("\n\n")
print (output2)

# if using the alternative method close file at end of script:
f.close()
