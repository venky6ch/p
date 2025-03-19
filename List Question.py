def find_triplet(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] * lst[j] * lst[k] == target:
                    return lst[i], lst[j], lst[k]
    return None


# Example usage:
lst = [12, 3, 27, 5, 4, 9, 4]
target = 180
result = find_triplet(lst, target)

if result:
    print("The three numbers are:", result)
else:
    print("No triplet found.")
