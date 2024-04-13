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

rows = len(matrix)
cols = len(matrix[0])

# Create a new matrix to store the transpose
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Print the transposed matrix
for row in transpose:
    print(row)
    