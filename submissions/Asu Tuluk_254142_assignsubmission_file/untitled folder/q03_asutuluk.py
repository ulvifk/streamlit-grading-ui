matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

original_matrix = [[1,2,3],[4,5,6]]
transposed_matrix = []

for i in range(len(original_matrix[0])):
    new_column = []

    for row in original_matrix:
        new_column.append(row[i])
    transposed_matrix.append(new_column)

print(f"The original matrix is: {original_matrix}")
print(f"The transposed matrix is: {transposed_matrix}")