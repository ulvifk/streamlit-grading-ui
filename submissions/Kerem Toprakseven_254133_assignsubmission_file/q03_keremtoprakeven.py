matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i]=matrix[i][j]
for row in transpose:
    print(row)

