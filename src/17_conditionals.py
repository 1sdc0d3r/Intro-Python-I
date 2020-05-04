x, y, z = 10, 50, 10
# * if
if x > y:
    print(f"{x} is greater than {y}")

# * if else
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

# * elif
if x > z:
    print(f"{x} is greater than {z}")
elif x == z:
    print(f"{x} is equal {z}")

else:
    print(f"{z} is greater than {x}")

# * and
if x > 2 and x <= 10:
    print(f"{x} is between range 3-10")

# * or
if x > 2 or x <= 10:
    print(f"{x} is 3+ or less or equal to 10")

# * not
if not(x == y):
    print(f"{x} doesn't equal {y}")


numbers = [n for n in range(1, 11)]

if x in numbers:
    print(x in numbers)

if y not in numbers:
    print(y not in numbers)


if x is z:
    print(x is z)

if x is not z:
    print(x is not z)
