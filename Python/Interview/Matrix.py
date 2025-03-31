# Multiply matrix
def multiply_matrices(A, B):
    # Dimensions of Matrix A and Matrix B
    m, n = len(A), len(A[0])
    n_b, p = len(B), len(B[0])

    # Ensure matrix dimensions are valid for multiplication
    if n != n_b:
        return "Matrix multiplication not possible. Number of columns in A must equal rows in B."

    # Initialize the resulting matrix with zeros
    result = [[0] * p for _ in range(m)]

    # Perform multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Example Input
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Output Result
result = multiply_matrices(A, B)
print("Resultant Matrix:")
for row in result:
    print(row)


# Fenced Matrix
import ast

mylist = ast.literal_eval(input())
rows, cols = (mylist[0], mylist[1])
dlist = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
            dlist[i][j] = 1


for i in range(rows):
    print(dlist[i])


# Withou buil-in, Transpose a matrix
# ---------------------------------------------
def transpose_matrix(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    columns = len(matrix[0])

    # Initialize a new matrix with the transposed dimensions
    transposed = [[0] * rows for _ in range(columns)]

    # Fill the transposed matrix by swapping rows and columns
    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]

    return transposed


# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in result:
    print(row)
