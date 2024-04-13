matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

transpose = list()

m = len(matrix)
n = len(matrix[0])

for i in range(n):
    new_rows = list()
    for j in range(m):
        new_rows.append(matrix[j][i])
    transpose.append(new_rows)
    
print(f'Transpose of the given matrix is:\n{transpose}')

