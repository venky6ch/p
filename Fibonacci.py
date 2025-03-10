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
