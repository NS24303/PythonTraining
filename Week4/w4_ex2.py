'''
Create three separate lists of IP addresses. The first list should be the IP addresses
of the Houston data center routers, and it should have over
ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers,
and it should have at least eight RFC1918 IP addresses (including some addresses
that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at
least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both
the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

houston = ['192.168.200.10',
           '10.20.30.40',
           '10.50.60.70',
           '10.80.90.100',
           '10.110.120.130,'
           '10.110.120.130',
           '10.140.150.160',
           '10.170.180.190',
           '10.200.210.220',
           '10.230.240.250']
atlanta = ['172.26.60.70',
           '172.26.90.100',
           '172.27.120.130,'
           '172.28.120.130',
           '172.29.150.160',
           '172.30.180.190',
           '10.200.210.220',
           '10.230.240.250']
chicago = ['192.168.200.10',
           '10.20.30.40',
           '172.27.120.130,'
           '172.28.120.130',
           '192.168.10.98,'
           '192.168.120.87',
           '192.168.230.160',
            '10.200.210.220',
           '192.168.77.190']

print(type(houston))

houston = set(houston)
atlanta = set(atlanta)
chicago = set(chicago)

print(houston)
print(atlanta)
print(chicago)

print("intersection of sets Houston & Atlanta \n" ,houston & atlanta,"\n")

print("intersection of sets Houston, Atlanta & chicago \n" ,houston & chicago & atlanta,"\n")

print("difference of sets is \n",chicago - atlanta - houston,"\n")
# could have used .difference rather than -, for example
print("difference of sets is \n",(chicago.difference(atlanta).difference(houston)),"\n")

