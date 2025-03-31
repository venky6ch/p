# ----------------------------------------------------------
#   Array vs List
import array
# import numpy as np

my_array = array.array("i", [1, 2, 3, 4, 5])  # array from the 'array' module
print(type(my_array))
print(isinstance(my_array, array.array))

# numpy_array = np.array([1, 2, 3, 4, 5]) # array from NumPy
# print(type(numpy_array))
# print(isinstance(numpy_array, np.ndarray))

my_list = [1, "hello", 3.14]
print(type(my_list))
print(isinstance(my_list, list))


# -----------------------------------------------------------
# Transpose Matrix
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = matrix
print(type(rows))

columns = matrix[2]
columns2 = matrix[0][1]

print(type(columns))
print(rows)
print(columns)
print(columns2)
"""


# -------------------------------------------------------
# 2 Sum problem
"""
nums = list(map(int, input("Enter space-separated integers: ").split()))
target = int(input("Enter the target sum: "))
for num in enumerate(nums):
    print(num)

"""

# -------------------------------------------------
# Print documentation string


# Even odd test
def even_odd(num):
    """This function will check whether a number is even or odd"""
    if num % 2 == 0:
        print(num, " is even number")
    else:
        print(num, " is odd number")


even_odd(3)
even_odd(4)
print(even_odd.__doc__)  # Print function documentation string
