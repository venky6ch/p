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
