def FindIntersection(strArr):
    """
    Finds the intersection of two lists of numbers provided as comma-separated strings.

    Parameters:
        strArr (list): A list containing two strings of comma-separated numbers.

    Returns:
        str: A comma-separated string of common numbers, or "false" if no intersection exists.
    """
    # Convert the input strings to lists of integers
    first_list = strArr[0].replace(" ", "").split(",")
    second_list = strArr[1].replace(" ", "").split(",")

    # Find common elements using set intersection
    intersection = [num for num in first_list if num in set(second_list)]

    # Return the result as a comma-separated string or "false" if empty
    return ",".join(intersection) if intersection else "false"


# Example usage
if __name__ == "__main__":
    user_input = input("Enter two strings of comma-separated numbers:\n").split(";")
    print(FindIntersection(user_input))


# ----------------------------   OR -------------------------------------
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
