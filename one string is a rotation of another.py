def is_rotation(s1, s2):
    # Check if lengths are equal
    if len(s1) != len(s2):
        return False
    # Concatenate s1 with itself
    combined = s1 + s1
    # Check if s2 is a substring of the concatenated string
    return s2 in combined


#  s1= "abcd"
#  s2="dabc"

# Example usage
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if is_rotation(s1, s2):
    print("Yes, the second string is a valid rotation of the first string.")
else:
    print("No, the second string is not a valid rotation of the first string.")
