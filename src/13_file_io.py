"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("foo.txt", "r") as foo:
    # print(foo.read())
    print('read')

#! r=read
#! r+=read/write
#! w=write
#! a=append

    # Open up a file called "bar.txt" (which doesn't exist yet) for
    # writing. Write three lines of arbitrary content to that file,
    # then close the file. Open up "bar.txt" and inspect it to make
    # sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "w") as bar:
    bar.write("Line 1\n")
    bar.write("Line 2\n")
    bar.write("Line 3\n")

with open("bar.txt", "a") as bar:
    bar.write("Line 4\n")
    bar.write("Line 5\n")
    bar.write("Line 6")

with open("bar.txt", "r") as bar:
    # print(bar.read())
    print("read")

# * creates file if not exits
myFile = open("myFile.txt", "w")

print("Name: '", myFile.name)
print("Is CLosed: '", myFile.closed)
print("Opening Mode: '", myFile.mode)

# * write to file
myFile.write("I love Python")
myFile.write(" and Javascript")
myFile.close()

# * Append to file
myFile = open("myFile.txt", "a")
myFile.write(" I also like Javascript")

# * Read from file
myFile = open("myFile.txt", "r+")
print(myFile.read(100))
