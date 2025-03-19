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
