def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = (
            char + reversed_s
        )  # Prepend each character to build the reversed string
    return reversed_s


# Example usage:
s = input("Enter a string: ")
print("Reversed string:", reverse_string(s))
