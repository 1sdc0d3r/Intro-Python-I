"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""
# x = 5       #int
# y = "7"     #str
# z = 3.5     #float
x, y, z = (5, "7", 3.5)

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
print(x + int(y))


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE

print(str(x) + y)

print(x + z + int(y))

print(id(x))  # points to postion in memory
