matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

matrix = [[1, 2, 3], [4, 5, 6]]

# Calculate the dimensions of the matrix
num_rows = len(matrix)
num_cols = len(matrix[0])

# Initialize the transpose matrix
transpose = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

# Compute the transpose of the matrix
for i in range(num_rows):
    for j in range(num_cols):
        transpose[j][i] = matrix[i][j]

# Print the transpose matrix
print("Transpose Matrix:")
for row in transpose:
    print(row)
