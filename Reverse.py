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
