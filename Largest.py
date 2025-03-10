# Second largest number
mylist = [10, 5, 5, 6, 7, 8, 9, 3, 8, 8, 8, 9, 9, 10, 10]
second_largest = list(sorted(set(mylist)))[-2]
print("Second Largest Number :- ", second_largest)
