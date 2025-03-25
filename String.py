# Matching 2 Letters
def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2
    print(lst)


common_letters()


# import sys

# print(sys.getsizeof("hello"))  # Returns size in bytes


# one string is a rotation of another
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


# Reverse Number
# take input of the number here
n = int(input())

# write code to reverse the number here
r = 0
while n > 0:
    r = r * 10 + n % 10
    n = n // 10
print(r)


# Reverse sentence

sentence = input()
list1 = sentence.split(" ")
list1.reverse()
print(" ".join(list1))


# The challenge here is to reverse a given string.
# The string can consist of whitespace and special symbols.
def FirstReverse(strParam):
    # code goes here
    strParam = strParam[::-1]
    return strParam


# keep this function call here
print(FirstReverse(input()))


# Split String at special character loc
Iam = "I,am!currently$ enrolled%in,data!science ^ course^Conducted  @UpGrad@IITB^Banglore^Karnataka"
spec_char = "@[_!#$%^&*()<>?/|,}{~:]"
index_list = []
for i in range(len(Iam)):
    if Iam[i] in spec_char:
        index_list.append(i)
final_list = []

for i in range(len(index_list)):
    if i < 1:
        final_list.append(Iam[0 : index_list[i]].strip())
    else:
        final_list.append(Iam[index_list[i - 1] + 1 : index_list[i]].strip())
final_list.append(Iam[index_list[i] + 1 : len(Iam)])
final_list


# Remove letters from  String


# Remove all duplicates from string


def removeChars(arr, string):
    # store characters of arr in a hash table
    hashTable = {}
    for c in arr:
        hashTable[c] = True
    # loop through the string and check if the character exists in
    # the hash table, if so, do not add it to the result string
    result = ""
    for c in string:
        if c not in hashTable:
            result += c
    return result


# usage
print(removeChars(["h", "e", "w", "o"], "hello world"))  # => "ll rld"


# Split String at special character loc
Iam = "I,am!currently$ enrolled%in,data!science ^ course^Conducted  @UpGrad@IITB^Banglore^Karnataka"
spec_char = "@[_!#$%^&*()<>?/|,}{~:]"
index_list = []
for i in range(len(Iam)):
    if Iam[i] in spec_char:
        index_list.append(i)
final_list = []

for i in range(len(index_list)):
    if i < 1:
        final_list.append(Iam[0 : index_list[i]].strip())
    else:
        final_list.append(Iam[index_list[i - 1] + 1 : index_list[i]].strip())
final_list.append(Iam[index_list[i] + 1 : len(Iam)])
final_list


# Vowel Test
vowels = "AaEeIiOoUu"
input_str = input("Enter String: ")
if input_str[0] in vowels:
    print("YES")
else:
    print("NO")


# Repeat 123a!

string = "123a!"


def create_duplicate(s):
    new_s = ""
    for char in s:
        new_s += str(char) * 2
    return new_s


print("Input data is string", string)
result = create_duplicate(string)
print("output", result)
