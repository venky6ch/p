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
