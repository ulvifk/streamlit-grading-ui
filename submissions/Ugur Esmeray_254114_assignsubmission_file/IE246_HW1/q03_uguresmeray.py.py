matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
# Original matrix of arbitrary size
matrix = [[3, 2, 5], [1, 3, 5]]  # Example matrix, you can replace it with any matrix

# Transposing the matrix
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Printing the transposed matrix
print("Original matrix:")
for row in matrix:
    print(row)
print("\nTransposed matrix:")
for row in transpose:
    print(row)

