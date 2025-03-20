def removeChars(arr, string):
    # store characters of arr in a hash table
    hashTable = {}
    for c in arr:
        hashTable[c] = True
    # loop through the string and check if the character exists in
    # the hash table, if so, do not add it to the result string
    result = ""
    for c in string:
        if c not in hashTable:
            result += c
    return result


# usage
print(removeChars(["h", "e", "w", "o"], "hello world"))  # => "ll rld"
