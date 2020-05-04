# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        pass


num = 12
# num = int(input("Enter a number: "))
print(is_even(num))


# Print out "Even!" if the number is even. Otherwise print "Odd" on user input
def even_odd(num):
    if(num % 2 == 0):
        return "Even"
    else:
        return "Odd"


# num = int(input("Enter a number: "))
print(even_odd(num))
