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
