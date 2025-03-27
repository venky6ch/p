def two_sum(nums, target):
    # Dictionary to store number and its index
    num_index = {}

    for i, num in enumerate(nums):
        # Calculate the complement that adds to the target
        complement = target - num
        if complement in num_index:
            # Return the indices of the two numbers
            return [num_index[complement], i]
        # Add the current number and its index to the dictionary
        num_index[num] = i

    return []  # Return an empty list if no solution is found


# Example usage:
nums = list(map(int, input("Enter space-separated integers: ").split()))
target = int(input("Enter the target sum: "))
result = two_sum(nums, target)
print("Indices of the two numbers:", result)
