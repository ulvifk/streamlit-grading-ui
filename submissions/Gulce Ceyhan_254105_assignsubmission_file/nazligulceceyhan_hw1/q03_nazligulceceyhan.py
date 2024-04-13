matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

new_transpose = []
for n in range(len(matrix[0])):
    rows_of_transpose = []
    for x in matrix:
        rows_of_transpose.append(x[n])
    new_transpose.append(rows_of_transpose)

transpose = new_transpose

print(transpose)    