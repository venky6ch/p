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


# Intersection of two lists or common elements between two lists
my_all_friends = ["userid1", "userid2", "userid3", "userid4"]
profile_friends = ["userid3", "userid4", "userid5", "userid6"]

mutual_friends = [i for i in my_all_friends if i in profile_friends]
print("Mutual Friends :-", mutual_friends)

# OR

my_all_friends = ["userid1", "userid2", "userid3", "userid4"]
profile_friends = ["userid3", "userid4", "userid5", "userid6"]

my_all_friends = set(["userid1", "userid2", "userid3", "userid4"])
profile_friends = set(["userid3", "userid4", "userid5", "userid6"])

mutual_friends = my_all_friends & profile_friends
mutual_friends


# Second largest number
mylist = [10, 5, 5, 6, 7, 8, 9, 3, 8, 8, 8, 9, 9, 10, 10]
second_largest = list(sorted(set(mylist)))[-2]
print("Second Largest Number :- ", second_largest)


# 0 Values to last in List
list = [1, 0, 4, 0, 5]
for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print(list)


# delete duplcate values


# Diff way to delete  values in List
