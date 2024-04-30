#!/usr/bin/python3

import os

import os

# Set the value of a custom environment variable using os.environ
os.environ['CUSTOM_VAR'] = 'custom_value'

# Retrieve and print the value of the custom environment variable using os.environ
custom_var_value = os.environ.get('CUSTOM_VAR')
print("Custom environment variable:", custom_var_value)

# Directly access os.environ to see if the environment variable is set
print("os.environ['CUSTOM_VAR']:", os.environ.get('CUSTOM_VAR'))

