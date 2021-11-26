import json
from pprint import pprint

my_list = list(range(10))
my_list.append('something')
my_list.append('another')

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

my_dict['key4'] = my_list
my_dict['key5'] = False

print(my_dict)
print(json.dumps(my_dict))

with open("my_file.json", "w") as f:
    json.dump(my_dict, f, indent=4)

filename = "my_file.json"

with open(filename) as f:
    json_data = json.load(f)

pprint(json_data)