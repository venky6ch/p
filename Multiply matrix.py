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
