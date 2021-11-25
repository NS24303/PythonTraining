import yaml
from pprint import pprint

filename = "my_devices.yml"
file_part2 = "more_devices.yml"

# using safe_load in the below code after reading this:
# https://stackoverflow.com/questions/69564817/typeerror-load-missing-1-required-positional-argument-loader-in-google-col

with open(filename) as f:
    output = yaml.safe_load(f)

print(output)
print(type(output))
#print(output[2])
print(output['rtr1'])
print("-"*65)

with open(file_part2) as f:
    output2 = yaml.safe_load(f)

pprint(output2)

