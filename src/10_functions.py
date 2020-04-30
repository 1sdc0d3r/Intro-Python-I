# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        pass


num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def even_odd(num):
    if(num % 2 == 0):
        return "Even"
    else:
        return "Odd"


num = input("Enter a number: ")
num = int(num)
print(even_odd(num))
