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
