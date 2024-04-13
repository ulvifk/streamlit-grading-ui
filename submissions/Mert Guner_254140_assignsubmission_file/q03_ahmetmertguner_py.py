matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

# Define the matrix
matrix = [[1, 2, 3], [4, 5, 6]]

# Get the dimensions of the matrix
m = len(matrix)
n = len(matrix[0])

# Initialize an empty list to store the transpose
transpose = []

# Iterate over columns of the matrix
for j in range(n):
    # Initialize an empty list to store the j-th column of the matrix
    column = []
    # Iterate over rows of the matrix
    for i in range(m):
        # Append the element at position (i, j) to the j-th column
        column.append(matrix[i][j])
    # Append the j-th column to the transpose
    transpose.append(column)

# Print the transpose
for row in transpose:
    print(row)
