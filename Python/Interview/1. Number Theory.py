# -------------------------------------------------------------------------------------
# Armstrong number Test

n = int(input("Enter the Number: "))
sum = 0
div = n
while div > 0:
    r = div % 10
    sum += r**3
    div = int(div / 10)
if sum == n:
    print("Armstrong number")
else:
    print("Not a Armstrong number")

# Exmaple1   153:    1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# Example2   370:    3³ + 7³ + 0³ = 27 + 343 + 0 = 370


# ---------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------
# The factorial of a number is the product of that number and every positive integer less than it.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1, or 120.


# Calculate factorial of a number using recursive function call.
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


# Calculate factorial using recursion
def fact(n):
    if n > 0:
        return n * fact(n - 1)
    else:
        return 1


print(fact(5))


# Calculate factorial
def fact(n):
    fact1 = 1
    for i in range(1, n + 1):
        fact1 *= i
    return fact1


print(fact(5))


# -----------------------------------------------------------------------
# Generate Fibonacci series

# The Fibonacci Sequence is a series of numbers starting with 0 and 1,
# where each succeeding number is the sum of the two preceding numbers. The sequence goes on infinitely.
#  Output   :    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89


def fiboacci(num):
    if num <= 1:
        return num
    if num == 2:
        return 1
    else:
        return fiboacci(num - 1) + fiboacci(num - 2)


nums = int(input("How many fibonacci numbers you want to generate -"))

#   Fibonacci
for i in range(nums):
    print(fiboacci(i))  # Generate Fibonacci series


# Fibonacci Series
n = int(input("Enter Number: "))
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


# ------------------------------------------------------------------------------------
# Sum of first n natural numbers
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(4))  # Sum of first five natural numbers (1,2,3,4),   1+2+3+4 = 10

# ------------------------------------------------------------------------------------------
# A palindrome number is a number that reads the same forward and backward.
# For example, 121, 1331, and 4554 are all palindrome numbers
# Palindrome
s = input("Enter Number: ")

print(s.lower() == s[::-1].lower())

# -------------------------------------------------------------------------------------------
#  it cannot be divided evenly by any other whole number besides 1 and itself.
# Examples: 2, 3, 5, 7, 11, 13, 17, 19 are prime numbers.
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
n = int(input("Enter Number : "))
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


# -----------------------------------------------------------------------------------------
# # write code to reverse the number here
# take input of the number here
n = int(input("Enter Number:"))

r = 0
while n > 0:
    r = r * 10 + n % 10
    n = n // 10
print("Reverse Number is: ", r)

# --------------------------------------------------------------------------------------------
# Without predefined functions Find Max


def find_max(numbers):
    max_num = numbers[0]  # Assume the first number is the maximum
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num


# Example usage
n = int(input("Enter number of elements: "))
numbers = list(map(int, input("Enter space-separated numbers: ").split()))
print(type(numbers))
print("The maximum number is:", find_max(numbers))


# ---------------------------------------------------------------------------------------------
# find the numbers that are Multiplication of 180


def find_triplet(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] * lst[j] * lst[k] == target:
                    return lst[i], lst[j], lst[k]
    return None


# Example usage:
lst = [12, 3, 27, 5, 4, 9, 4]
target = 180
result = find_triplet(lst, target)

if result:
    print("The three numbers are:", result)
else:
    print("No triplet found.")
