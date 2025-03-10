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
