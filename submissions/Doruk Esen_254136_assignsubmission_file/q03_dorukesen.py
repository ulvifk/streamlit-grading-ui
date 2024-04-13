matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

outer = len(matrix)
inner = len(matrix[0])
transpose = [[0 for i in range(outer)] for j in range(inner)]
for i in range(outer):
    for j in range(inner):
        transpose[j][i] = matrix[i][j]
print (transpose)