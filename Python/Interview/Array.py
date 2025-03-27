#  Array Adding correct position


def insert_in_sorted_array(arr, element):
    # Find the position where the element should be inserted
    for i in range(len(arr)):
        if arr[i] > element:
            # Insert element at the correct position
            return arr[:i] + [element] + arr[i:]
    # If element is larger than all, append it at the end
    return arr + [element]


# Example usage
arr = list(
    map(int, input("Enter space-separated integers: ").split())
)  # [3, 6, 8, 12, 15]
element = int(input("Enter the Number: "))  # 7
result = insert_in_sorted_array(arr, element)
print("Array after insertion:", result)

"""
In Python, an array is typically implemented using the array module, 
while a list is the built-in dynamic data structure that can hold heterogeneous elements. 
Since you're using standard list operations like slicing (arr[:i] + [element] + arr[i:]) and the append operation,
this is a list-based implementation, not an actual array.

"""
# If you need an array, you can use the array module like this:

import array


def insert_in_sorted_array(arr, element):
    for i in range(len(arr)):
        if arr[i] > element:
            return arr[:i] + array.array(arr.typecode, [element]) + arr[i:]
    return arr + array.array(arr.typecode, [element])


# Example usage
arr = array.array("i", [3, 6, 8, 12, 15])  # 'i' denotes an array of integers
element = int(input("Enter the Number: "))  # Example: 7
result = insert_in_sorted_array(arr, element)
print("Array after insertion:", list(result))  # Convert to list for display


# -----------------------------------------------------------------
# Array finding the length of increasing subsequence
def longest_increasing_subsequence(arr):
    from bisect import bisect_left

    # Initialize an empty list to store the current longest subsequence
    subseq = []

    for num in arr:
        # Find the position where `num` can be inserted in `subseq`
        pos = bisect_left(subseq, num)
        if pos == len(subseq):
            subseq.append(num)  # Extend the subsequence
        else:
            subseq[pos] = num  # Replace the element to keep the subsequence minimal

    return len(subseq)


# Example usage
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
print(
    "Length of the longest strictly increasing subsequence:",
    longest_increasing_subsequence(arr),
)


# -------------------------------------------------------------
# Merged and sorted array
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
