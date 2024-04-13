matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

def transpose_matrix(matrix):
    # Get the dimensions of the original matrix
    m = len(matrix)
    n = len(matrix[0])

    # Create the transpose matrix
    transpose = [[matrix[j][i] for j in range(m)] for i in range(n)]
    
    return transpose

# Example matrix
matrix = [[1, 2, 3], [4, 5, 6]]

# Transpose the matrix
transpose = transpose_matrix(matrix)

# Print the transposed matrix
for row in transpose:
    print(row)
