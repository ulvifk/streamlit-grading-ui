matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

rows = len(matrix)
cols = len(matrix[0])

transpose = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

for row in transpose:
    print(row)
