'''
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password.
 The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.

1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default
value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
'''

def ssh_conn_a():
    # initial funciton
    ip_addr = "172.16.44.50"
    username = "max"
    password = "admin"
    device_type ="cisco_ios"
    print("ip_addr:", ip_addr)
    print("username:", username)
    print("password:", password)
    print("Device Type:", device_type)

def ssh_conn_b(ip_addr, username, password):
    # positional arguments
    print("-"*65)
    print("-"*20, "Positional arguments")
    print("ip_addr:", ip_addr)
    print("username:", username)
    print("password:", password)

def ssh_conn_c(ip_addr, username, password):
    # named arguments
    print("-"*65)
    print("-"*20, "Named arguments")
    print("ip_addr:", ip_addr)
    print("username:", username)
    print("password:", password)

def ssh_conn_d(ip_addr, username, password):
    # positional and named arguments
    print("-"*65)
    print("-"*20, "Postitional & Named arguments")
    print("ip_addr:", ip_addr)
    print("username:", username)
    print("password:", password)

def ssh_conn_e(ip_addr, username, password,device_type='cisco_ios'):
    # **kwargs technique
    print("-"*65)
    print("-"*20, "Postitional & Named arguments")
    print("ip_addr:", ip_addr)
    print("username:", username)
    print("password:", password)
    print("Device_type:", device_type)

ssh_conn_a()
ssh_conn_b("10.5.6.7", "bob", "random_pass")
ssh_conn_c(password = "something", ip_addr = "192.168.6.7", username = "fred")
ssh_conn_d("10.52.25.63", password = "another",  username = "jane")

my_dict = {
    'ip_addr': '172.16.78.3',
    'username': 'emma',
    'password': 'random',
    'device_type': 'junos'
    # over write the default cisco_ios
}

ssh_conn_e(**my_dict)
