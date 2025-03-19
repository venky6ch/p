string = "123a!"


def create_duplicate(s):
    new_s = ""
    for char in s:
        new_s += str(char) * 2
    return new_s


print("Input data is string", string)
result = create_duplicate(string)
print("output", result)
