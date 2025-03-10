mystr4 = "one two three four one two two three five five six seven six seven one one one ten eight ten nine eleven ten ten nine"
mylist = mystr4.split()  # Split String into substrings
mylist1 = set(mylist)  # Unique values in a list
mylist1 = list(mylist1)


# Calculate frequenct of each word
count1 = [0] * len(mylist1)
mydict5 = dict()
for i in range(len(mylist1)):
    for j in range(len(mylist)):
        if mylist1[i] == mylist[j]:
            count1[i] += 1
    mydict5[mylist1[i]] = count1[i]
print(mydict5)
