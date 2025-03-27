"""
The values are not swapping in your code because Python passes variables to functions by value,
but for mutable objects (like lists or dictionaries), the reference is passed,
whereas for immutable objects (like integers), a copy of the value is passed.

In this case:
Immutable Variables (a and b):
When you call swap(a, b), the values of a and b are copied and passed to the function.
Inside the swap function, these are treated as local variables.
The original a and b from outside the function are unaffected.

Breaking the Link:
Inside the swap function, you're swapping the local copies of a and b.
However, this doesn't change the values of a and b outside the function.
"""


def swap(a, b):
    temp = a
    a = b  # link of 'a' with previous object is broken now as new object is assigned to 'a'.
    b = temp  # link of 'b' with previous object is broken now as new object is assigned to 'b'.
    return b, a


a = 10
b = 20
print("Before swap: a =", a, ", b =", b)

# Swap values
a, b = swap(a, b)
print("After swap: a =", a, ", b =", b)


# other way
"""

x, y = 10, 50
temp = x
x = y
y = temp

print("x:", x)
print("y:", y)
"""
