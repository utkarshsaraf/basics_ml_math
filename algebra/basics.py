# Define two vectors
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

# Initialize the inner product variable
inner_product_manual = 0

# Calculate the inner product step by step
for i in range(len(vector_a)):
    product = vector_a[i] * vector_b[i]  # Multiply corresponding elements
    print(f"Multiplying: {vector_a[i]} * {vector_b[i]} = {product}")
    inner_product_manual += product  # Accumulate the sum

# Print the final result
print("Inner Product (Manual Calculation):", inner_product_manual)
