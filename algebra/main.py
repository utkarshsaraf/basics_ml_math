import numpy as np

# Creating a row vector
row_vector = np.array([[1, 2, 3, 4, 5]])

print("Row vector:", row_vector)

# Creating a column vector
column_vector = np.array([[1], [2], [3], [4], [5]])

print("Column vector:\n", column_vector)

# 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("3x3 Matrix:\n", matrix_3x3)

# Creating a 4x4 identity matrix
identity_matrix = np.eye(4)

print("4x4 Identity Matrix:\n", identity_matrix)

# Creating a diagonal matrix with specified diagonal values
diagonal_matrix = np.diag([1, 2, 3, 4])

print("Diagonal Matrix:\n", diagonal_matrix)

# Generate a random 3x3 matrix
A = np.random.rand(3, 3)

# Make the matrix symmetric by averaging it with its transpose
symmetric_matrix = (A + A.T) / 2

print("Symmetric Matrix:\n", symmetric_matrix)


# Define two vectors
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Calculate the inner product
inner_product = np.dot(vector_a, vector_b)

print("Inner Product (scalar):", inner_product)

import numpy as np

# Example matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute SVD
U, S, VT = np.linalg.svd(A)

# S is returned as a 1D array, converting it to a diagonal matrix
Sigma = np.zeros_like(A, dtype=float)
np.fill_diagonal(Sigma, S)

print("U Matrix:\n", U)
print("Sigma Matrix:\n", Sigma)
print("V^T Matrix:\n", VT)

