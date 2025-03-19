def merge_and_sort_arrays(arr1, arr2):
    # Combine both arrays
    merged_array = arr1 + arr2
    # Sort the combined array
    merged_array.sort()
    return merged_array


# Example usage:
arr1 = [3, 1, 5, 9]
arr2 = [8, 2, 6, 4]
result = merge_and_sort_arrays(arr1, arr2)
print("Merged and sorted array:", result)


#      -------      OR -------------------
def merge_and_sort_arrays(arr1, arr2):
    # Merge the two arrays
    merged_array = arr1 + arr2

    # Perform Bubble Sort on the merged array
    n = len(merged_array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged_array[j] > merged_array[j + 1]:
                # Swap if the element is greater than the next element
                merged_array[j], merged_array[j + 1] = (
                    merged_array[j + 1],
                    merged_array[j],
                )

    return merged_array


# Example usage
arr1 = [3, 1, 5, 9]
arr2 = [8, 2, 6, 4]
result = merge_and_sort_arrays(arr1, arr2)
print("Merged and sorted array:", result)
