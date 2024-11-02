import numpy as np

# Define the vector v and the matrix X
v = np.array([3, 4])
X = np.array([[1, 1], [1, 2]])  # Column vectors x1 and x2

# Calculate the projection matrix P
X_pseudo_inverse = np.linalg.pinv(X)  # Pseudo-inverse of X
P = X @ X_pseudo_inverse  # Projection matrix

# Project v onto the subspace spanned by X
projection_subspace = P @ v


# Project v onto each column of X separately and sum the projections
def project_onto_column(v, x):
    return (np.dot(v, x) / np.dot(x, x)) * x


projection_separate = project_onto_column(v, X[:, 0]) + project_onto_column(v, X[:, 1])

# Print the results
print("Projection onto the subspace spanned by columns of X:")
print(projection_subspace)

print("\nSum of projections onto each column separately:")
print(projection_separate)

# Check if they are the same
are_equal = np.allclose(projection_subspace, projection_separate)
print("\nAre the two projections equal?", are_equal)
