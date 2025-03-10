# Armstrong number Test
n = int(input())
sum = 0
div = n
while div > 0:
    r = div % 10
    sum += r**3
    div = int(div / 10)
print(sum == n)
