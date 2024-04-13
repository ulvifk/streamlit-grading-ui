matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
transpose = []

for i in range(len(matrix[0])):
    new_row = []
    for k in matrix:
        new_row.append(k[i])
    transpose.append(new_row)

print(f"Your original matrix is {matrix}")
print(f"Your transposed matrix is {transpose} ")