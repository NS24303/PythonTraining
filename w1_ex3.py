ipvsix_a = str("1001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPVSIX_B = str("2001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPv6_C = str("3001:0000:3238:DFE1:0063:0000:0000:FEFB")

print(ipvsix_a)
print(IPVSIX_B)
print(IPv6_C)

print("Does IPv6_a and IPv6_b match?: " ,ipvsix_a == IPVSIX_B)
print("Does IPv6_a note match IPv6_b ?: " ,ipvsix_a != IPVSIX_B)