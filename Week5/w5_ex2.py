'''
Create a function that randomly generates an IP address for a network.
The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet:
import random
random.randint(1, 254)

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
'''

import random

def random_ip(subnet='10.10.10.'):
    last_oct = str(random.randint(1,254))
    ip_addr = subnet + last_oct
    print("Your IP Address is:", ip_addr)


random_ip()
random_ip("9.9.9.")
random_ip(subnet = "8.8.8.")


'''
overall the above code works but a better way to do the function would have been using the 
return statement to end the function. 

If I had done this I could have reduced the function to 2 lines and used 

print(random_ip())

for example:
def random_ip(subnet='10.10.10.'):
    last_oct = str(random.randint(1,254))
    return subnet + last_oct
    
    
print(random_ip("44.44.44.")) 

'''