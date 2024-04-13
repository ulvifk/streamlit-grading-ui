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
transpose = []

rows1 = len(matrix)
cols1 = len(matrix[0])

for j in range(cols1):
    transpose_row = []
    for i in range(rows1):
        transpose_row.append(matrix[i][j])
    transpose.append(transpose_row)

for row in transpose:
    print(row)
