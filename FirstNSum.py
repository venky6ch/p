def add(num):  # Sum of first n natural numbers
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(6))  # Sum of first five natural numbers (1,2,3,4,5,6)
