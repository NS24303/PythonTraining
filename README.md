# PythonTraining
Initial training with Python &amp; Git

### one.py
random stuff

### one.py
random stuff

### ip_in_bin_hex.py
Takes an ip address
- splits it into octets
- outputs as binary
- outputs as hex

### show_ver.py
script for taking a fixed output and performing following:
- strip leading and trialing whitespace
- split output to grab model and serial
- convert field to lower case
- perform boolean check on output

### arp_table_format.py
Take formatted output of arp and format into table 

### files.py
Initial testing of using external files with python scrips

### lists.py
- demo of simple lists
- tuples
- splits & joins
- import sys (arguments )

## Week1

### w1_ex1.py
- import sys
- formatting of output
- python2/python3 user input method
- output formatting 

### w1_ex2.py
- user input
- conversion to binary and hex
- output formatting 

### w1_ex3.py
- IPv6 variables
- Boolean verification

### w1_ex4.py
- changing case
- split & strip method
- Boolean verification

### w1_ex5.py
- formatting of text

## Week2

### w2_ex1.py
- File open & closes. Both methods

### w2_ex2.py
- lists
    - extend, append & concatenation & pop

### w2_ex3.py
- import of pretty print (pprint)
- files (open & write)
- lists
  - sort
- join

### w2_ex4.py
- File Opens
- Spilt method
- Tuples
- pycodestyle (linter)

### w2_ex5.py
- File Opens
  - spilt, rstrip
- lists
- num2words

## Week3

### w3_general.py
- ternary operator (conditional expressions)
- None Data type
- for loops
  - breaks
  - range
  - else
  - enumerate
- while loops
  - breaks

## Week3

### w3_ex1.py

- pprint
- reading from file
  - for loop
  - if statement with continue
  - startswith method
  - split
  - splitline

### w3_ex1.py

- reading from file
  - for loop
  - if statement
    - contine & break

### w3_ex2.py

- reading from file
  - for loop
  - if statement
    - contine & break
    - elif
    - 
### w3_ex3.py

- reading from file
  - for loop
  - if statement
    - contine & break
    - elif
- format method for print statments 

### w3_ex4.py

- if & while loop
- join
- split
- replace
- upper
- append

### w3_ex5.py

- ping script
- import os (detect operating system)
- for & while loop 
  - enumerate
  - append
- Ternary operator 

## Week4
  
### w4_general.py

- Dictionaries
  - get method
  - pop
  - update
  - values & keys
- Sets
  - union '|' (all elements from both, ignore duplicates)
  - intersection '&' (elements common to both sets)
  - difference '-' (anything that is common removed from first set) 
  - symmetric difference '^' (XOR, nothing common between two sets, only unique)
- Exceptions
  - try
  - KeyError (dict)
  - IndexError (list)
  - Exception (any error)

### w4_regex.py

- Regular Expressions
- re.search
  - group
  - groupdict
  - multi line flag (re.M)
  - Match new lines (re.DOTALL)
  - ignore case (re.I)
  - split (re.split)
  - substitution (re.sub)
  - find all (re.findall)
- named RegEx (?P)
  
### w4_ex1.py

- dict & .update method
- for loop
- if

### w4_ex2.py

- Sets with intersections & differences

### w4_ex3.py

- RegEx matching output from show_version

### w4_ex4.py

- Named RegEx

### w4_ex5.py

- RegEx with DOTALL
  - strip
  - splitline
  - for loop

## Week5

### w5_general.py

- functions
  - named arguments
  - positional arguments
- Classes
- List comprehension 
- lambda functions
- Debugging (pdb)

### w5_ex1.py

- functions
  - named arguments
  - positional arguments
  - **kwargs technique

### w5_ex2.py

- functions
- import random
- type casting
  - positional arguments
  - **kwargs technique

### w5_ex3.py

- functions
  - regex
  - if statements
  - zfill
  - raise (error)
  - split & append

## Week6

### W6_general.py
### W6_delay.py
### W6_multiline.py
- Netmiko
  - delay_factor
  - global_delay_factor
  - send_command
  - send_command_timing
- getpass

### list_device_type.py

- full list of devices in Netmiko

### W6_testFSM.py

- Sample script using TextFSM to format output

## Week7

### w7_general.py

- Jinja2 - configuration templates

### w7_general2.py

- jinja2 - import from file
  - for loop
  - conditional
  
### w7_general3.py

- jinja2 external csv variable file 

### w7_output_test.py

- Creating Jinja2 templates and outputting to file per csv line

### w7_general4py

- jinja2 nested for & if loops

### w7_yaml.py

- reading a yaml file into python

### w7_py_2_yaml.py

- converting python to yaml

### w7_yaml.py

- converting python to JSON 