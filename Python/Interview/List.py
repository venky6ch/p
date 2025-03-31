# -------------------------------------------------------------------------------------
# Without / Without buil- in, List insert & Delete


def insert_element(lst, index, element):
    # Insert element at a specific index
    lst = lst[:index] + [element] + lst[index:]
    return lst


def delete_element(lst, index):
    # Delete element at a specific index
    lst = lst[:index] + lst[index + 1 :]
    return lst


print("Without built- in, List insert & Delete")
print("----------------------------------------")
# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Insert element 10 at index 2
my_list = insert_element(my_list, 2, 10)
print("After Insertion:", my_list)

# Delete element at index 3
my_list = delete_element(my_list, 3)
print("After Deletion:", my_list)

print("With built- in, List insert & Delete")
print("----------------------------------------")

# Example usage
my_list2 = [1, 2, 3, 4, 5]
print("Original List:", my_list2)

my_list2.insert(2, 10)  # Add item at index location 1
print("After Insertion:", my_list2)


my_list2.pop(3)  # Remove item at index location 8
print("After Deletion:", my_list2)


# ----------------------------------------------------------------------------------------


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
print("Without built- in")
print("----------------------------------------")
n = int(input("Enter the number of elements in the list: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
print("The second largest number is:", find_second_largest(numbers))


# with using the built-in, Second largest
print("With built- in")
print("----------------------------------------")
a = [10, 20, 4, 45, 99]
print("List elemetns: ", a)
# Sorting the list in descending order
a.sort(reverse=True)

# Second largest number will be at index 1
print("The second largest number is:", a[1])


# Scenario 2 : Second largest number
mylist = [10, 5, 5, 6, 7, 8, 9, 3, 8, 8, 8, 9, 9, 10, 10]
second_largest = list(sorted(set(mylist)))[-2]
print("Scenario 2 : Second Largest Number :- ", second_largest)


# --------------------------------------------------------------------------------------------

# without using the built-in Sum of List


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number  # Add each number to the total
    return total


# Example usage
print("Without built- in")
print("----------------------------------------")
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
print("The sum of the numbers is:", calculate_sum(numbers))


# with using the built-in Sum of List
numbers1 = [1, 2, 3]
Sum1 = sum(numbers1)
print("With built- in")
print("----------------------------------------")
print("The sum of the numbers is:", Sum1)


# ----------------------------------------------------------------------------------------
#  Without Using sort or sorted Sorting list


def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]  # Swap elements
    return numbers


# Example usage:
print("----------------------------------------")
print("With built- in")
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter space-separated integers: ").split()))
sorted_numbers = sort_list(numbers)
print("Without Using sort or sorted Sorting list", (" ".join(map(str, sorted_numbers))))


# With built- in sort
print("----------------------------------------")
print("With built- in sort")
prime_numbers = [3, 5, 2]
print("Before With Using sort", prime_numbers)
# sort the list in ascending order
prime_numbers.sort()
print("After With Using sort", prime_numbers)


# "With built- in sorted
print("----------------------------------------")
print("With built- in sorted")
list1 = [1, 4, 2, 4]
print("Before With Using sorted ", list1)
s1 = sorted(list1)
print(" After With Using sorted ", s1)


# --------------------------------------------------------------------


# Without Set, Remove Duplcate from List
def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


# Example usage:
print("----------------------------------------")
print("Without built- in")
n = int(input("Enter the number of elements in the list: "))
input_list = input("Enter the list elements (space-separated): ").split()
result = remove_duplicates(input_list)
print("List after removing duplicates:", " ".join(result))


# With Set, Remove Duplcate from List
list1 = [1, 2, 3, 3, 4, 4]
s1 = set(list1)
l1 = list(s1)
print("----------------------------------------")
print("With built- in")
print(s1)
print("Convert Set to List")
print(l1)


# -------------------------------------------------------------
# Adding 0 Values to last in List
list = [1, 0, 4, 0, 5]
for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print(list)


# -------------------------------------------------------------

# Intersection of two lists or common elements between two lists
my_all_friends = ["userid1", "userid2", "userid3", "userid4"]
profile_friends = ["userid3", "userid4", "userid5", "userid6"]

mutual_friends = [i for i in my_all_friends if i in profile_friends]
print("----------------------------------------")
print("Without built- in, List Comprehensions")
print("Mutual Friends :-", mutual_friends)

# OR-----------

my_all_friends = ["userid1", "userid2", "userid3", "userid4"]
profile_friends = ["userid3", "userid4", "userid5", "userid6"]
mutual_friends = []
for i in my_all_friends:
    if i in profile_friends:
        mutual_friends.append(i)
print("----------------------------------------")
print("Without built- in, List without Comprehensions")
print("Mutual Friends :-", mutual_friends)


# OR--------------
print("----------------------------------------")
print("With built- in Using Set")
my_all_friends = ["userid1", "userid2", "userid3", "userid4"]
profile_friends = ["userid3", "userid4", "userid5", "userid6"]

my_all_friends = set(["userid1", "userid2", "userid3", "userid4"])
profile_friends = set(["userid3", "userid4", "userid5", "userid6"])

mutual_friends = my_all_friends & profile_friends
print("Using Set Mutual Friends :-", mutual_friends)
