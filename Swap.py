def swap(a, b):
    temp = a
    a = b  # link of 'a' with previous object is broken now as new object is assigned to 'a'.
    b = temp  # link of 'b' with previous object is broken now as new object is assigned to 'b'.


a = 10
b = 20
swap(a, b)
print("print a", a)
print("print b", b)

# other way

x, y = 10, 50

temp = x
x = y
y = temp

print("x:", x)
print("y:", y)
