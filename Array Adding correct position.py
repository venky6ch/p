def insert_in_sorted_array(arr, element):
    # Find the position where the element should be inserted
    for i in range(len(arr)):
        if arr[i] > element:
            # Insert element at the correct position
            return arr[:i] + [element] + arr[i:]
    # If element is larger than all, append it at the end
    return arr + [element]


# Example usage
arr = [3, 6, 8, 12, 15]
element = 7
result = insert_in_sorted_array(arr, element)
print("Array after insertion:", result)
