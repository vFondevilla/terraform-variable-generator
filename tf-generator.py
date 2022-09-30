#!python
import sys
import os
import re
import hcl2
import json


## This script will read the Terraform files and create a list of all the variables
## that are used in the Terraform files.
##

tosearch = 'var.'
variables = []
def open_file(filename):
	with open(filename, 'r') as f:
		# dict = hcl2.load(f)
		# print(dict)
		return f.read()
		# return dict

## This function will parse each line of the Terraform file and return a list of all the variables,
## the variables can be anywhere on the line
def parse_variables(file):
	for line in file.splitlines():
		if tosearch in line:
			# found = (line.split(tosearch)[1].split()[0] and line.split(tosearch)[1].split("}")[0])
			found = (re.split('var.', line)[1]) 
			found = (re.split(r"[^a-zA-Z0-9\s_-]", found)[0])
			if found not in variables:
				variables.append(found)
	return variables

## This function will print the variable file to the screen
def print_variables(variables):
	variables.sort()
	for variable in variables:
		print(f"variable {variable} {{}}")


for file in os.listdir(sys.argv[1]):
	if file.endswith(".tf"):
		variables = parse_variables(open_file(file))
		# print(variables)
print_variables(variables)