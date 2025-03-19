def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number  # Add each number to the total
    return total


# Example usage
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
print("The sum of the numbers is:", calculate_sum(numbers))
