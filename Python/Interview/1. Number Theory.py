# Armstrong number Test
n = int(input())
sum = 0
div = n
while div > 0:
    r = div % 10
    sum += r**3
    div = int(div / 10)
print(sum == n)


# Even odd test
def even_odd(num):
    """This function will check whether a number is even or odd"""
    if num % 2 == 0:
        print(num, " is even number")
    else:
        print(num, " is odd number")


even_odd(3)
even_odd(4)
print(even_odd.__doc__)  # Print function documentation string


# Calculate factorial of a number using recursive function call.
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(6))


# Calculate factorial using recursion
def fact(n):
    if n > 0:
        return n * fact(n - 1)
    else:
        return 1


fact(4), fact(3), fact(5)


# Calculate factorial
def fact(n):
    fact1 = 1
    for i in range(1, n + 1):
        fact1 *= i
    return fact1


fact(4), fact(3), fact(5)


# Generate Fibonacci series


def fiboacci(num):
    if num <= 1:
        return num
    if num == 2:
        return 1
    else:
        return fiboacci(num - 1) + fiboacci(num - 2)


nums = int(input("How many fibonacci numbers you want to generate -"))


for i in range(nums):
    print(fiboacci(i))  # Generate Fibonacci series


####################
#           OR
#################

# Fibonacci Series
n = int(input())
# write your code here
prev = 0
nxt = 1
if n > 0:
    print(0)
if n > 1:
    print(1)
if n > 2:
    for i in range(3, n + 1):
        nxt = prev + nxt
        print(nxt)
        prev = nxt - prev


# Sum of first n natural numbers
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(6))  # Sum of first five natural numbers (1,2,3,4,5,6)


# Second largest number
mylist = [10, 5, 5, 6, 7, 8, 9, 3, 8, 8, 8, 9, 9, 10, 10]
second_largest = list(sorted(set(mylist)))[-2]
print("Second Largest Number :- ", second_largest)


# Palindrome
s = input()

print(s.lower() == s[::-1].lower())


# Print all prime numbers betweem 1 - 20
for i in range(1, 20):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=",")


# Sum of prime numbers from 2 to n
n = int(input())
sum = 0
for i in range(2, n + 1):
    flag = True
    for j in range(2, int(n / 2) + 1):
        if i % j == 0 and i != j:
            flag = False
            break
    if flag:
        sum += i
print(sum)


# Sum of first n natural numbers
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


add(5)  # Sum of first five natural numbers (1,2,3,4,5)
