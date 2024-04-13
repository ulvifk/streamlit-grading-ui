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


rows = len(matrix)
columns = len(matrix[0])
    
transpose = []
for j in range(columns):
    a = []
    for i in range(rows):
        x = matrix[i][j]
        a.append(x)
    transpose.append(a)
    
print(f"transpose: {transpose}")
