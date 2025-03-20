def FindIntersection(strArr):
    # converting strings to lists of int
    len1 = strArr[0].replace(" ", "").split(",")
    len2 = strArr[1].replace(" ", "").split(",")

    # finding the common numbers
    temp = set(len2)
    len = [i for i in len1 if i in temp]

    # convert back to string
    if len:
        return ",".join(len)
    else:
        return "false"


# keep this function call here
print(FindIntersection(input()))
