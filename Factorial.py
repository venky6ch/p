def factorial(num):  # Calculate factorial of a number using recursive function call.
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(3))
