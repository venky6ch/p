def insert_element(lst, index, element):
    # Insert element at a specific index
    lst = lst[:index] + [element] + lst[index:]
    return lst


def delete_element(lst, index):
    # Delete element at a specific index
    lst = lst[:index] + lst[index + 1 :]
    return lst


# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Insert element 10 at index 2
my_list = insert_element(my_list, 2, 10)
print("After Insertion:", my_list)

# Delete element at index 3
my_list = delete_element(my_list, 3)
print("After Deletion:", my_list)


# --------------------------------------------------------------------


# without using the built-in, Second largest
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


# ----------------------------


# without using the built-in Sum of List


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number  # Add each number to the total
    return total


# Example usage
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
print("The sum of the numbers is:", calculate_sum(numbers))


# -------------------------------------------------------------

#  Without Using sort or sorted Sorting list


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


# -------------------------------


# Without Set, Remove Duplcate from List
def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


# Example usage:
n = int(input("Enter the number of elements in the list: "))
input_list = input("Enter the list elements (space-separated): ").split()
result = remove_duplicates(input_list)
print("List after removing duplicates:", " ".join(result))


# ----------------------------


#  Without using the built-in reverse a string
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = (
            char + reversed_s
        )  # Prepend each character to build the reversed string
    return reversed_s


# Example usage:
s = input("Enter a string: ")
print("Reversed string:", reverse_string(s))
