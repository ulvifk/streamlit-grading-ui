matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################


row_mat = len(matrix)
col_mat = len(matrix[0])

transpose = [[matrix[j][i] for j in range(row_mat)] for i in range(col_mat)]

for row in transpose:
    print(row)