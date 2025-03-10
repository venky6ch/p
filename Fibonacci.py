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
