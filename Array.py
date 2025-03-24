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
arr = [3, 6, 8, 12, 15]
element = 7
result = insert_in_sorted_array(arr, element)
print("Array after insertion:", result)


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
