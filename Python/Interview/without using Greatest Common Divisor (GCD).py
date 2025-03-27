def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The Greatest Common Divisor is:", find_gcd(a, b))
