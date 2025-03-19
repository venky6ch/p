def find_second_largest(numbers):
    # Initialize variables for the largest and second largest
    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


# Example usage
n = int(input("Enter the number of elements in the list: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
print("The second largest number is:", find_second_largest(numbers))
