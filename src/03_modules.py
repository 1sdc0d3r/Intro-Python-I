"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
# * Core modules
import os
import sys
from datetime import date
from time import time

# * Pip module
from camelcase import CamelCase

# * Custom module
from validator import validate_email
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# for arg in sys.argv:
# print(arg)
print(sys.argv[0])

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
# Linux: Linux
# Mac: Darwin
# Windows: Windows

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())


today = date.today()
print(today)

timestamp = time()
print(timestamp)

c = CamelCase()
print(c.hump("hello there world"))

email = 'test@test.com'

if validate_email(email):
    print("Email is valid")
else:
    print("Email is bad")
