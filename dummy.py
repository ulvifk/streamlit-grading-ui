matrix = [[3, 2, 5], [1, 3, 5]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

nrow, ncol = len(matrix), len(matrix[0])
transpose = [[0]*nrow for i in range(ncol)]
a = 0
b = 0
while b < nrow :
    a = 0
    while a < ncol :
        transpose[a][b] = matrix[b][a]
        a += 1
    b += 1
print(transpose)
 
