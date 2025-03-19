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
