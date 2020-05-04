# For the exercise, look up the methods and functions that are available for use
#! A List is a collection which is ordered and changeable. Allows duplicate members
# with Python lists.

# x = [1, 2, 3]
# y = [8, 9, 10]
x, y = ([1, 2, 3], [8, 9, 10])

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("append 4", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# * x = x+y

# * for n in y:
# *     x.append(n)

x = [n for n in x+y]
print("append x, y", x)


# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# * x.remove(8)
# * x.pop(4)
# * x.pop(-3)
del x[4]
print("del index 4", x)


# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(-1, 99)
print("insert 99", x)


# Print the length of list x
# YOUR CODE HERE
print("len x", len(x))


# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# * for num in x:
# *     print(num*1000)

x = [num*1000 for num in x]
print("mult x", x)

fruits = ["Apples", "Oranges", "Pears", "Mangos"]

print("--------------------------------------------")
print("fruits", fruits)

fruits.reverse()
print("reverse", fruits)

fruits.sort()
print("sort", fruits)

fruits.sort(reverse=True)
print("reverse sort", fruits)
