def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]  # Swap elements
    return numbers


# Example usage:
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
sorted_numbers = sort_list(numbers)
print(" ".join(map(str, sorted_numbers)))
