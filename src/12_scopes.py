# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x(var):
    var = 99
    print(var)


change_x(x)

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        # ? nonlocal
        y = 999
        # print(y)
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()


def scope_test():
    def do_local():
        spam = "local spam"
        # local assignment (default) didn’t change scope_test’s binding of spam

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        # nonlocal assignment changed scope_test’s binding of spam

    def do_global():
        global spam
        spam = "global spam"
        # global assignment changed the module-level binding

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
