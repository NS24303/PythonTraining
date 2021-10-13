''' Create three different variables the first variable should use all lower case characters with underscore ( _ )
 as the word separator. The second variable should use all upper case characters with underscore as the word separator.
 The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

ipvsix_a = str("1001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPVSIX_B = str("2001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPv6_C = str("3001:0000:3238:DFE1:0063:0000:0000:FEFB")

print(ipvsix_a)
print(IPVSIX_B)
print(IPv6_C)

print("Does IPv6_a and IPv6_b match?: " ,ipvsix_a == IPVSIX_B)
print("Does IPv6_a note match IPv6_b ?: " ,ipvsix_a != IPVSIX_B)