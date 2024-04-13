matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################


m = len(matrix)
n = len(matrix[0])

transpose = []

for j in range(n):  
    column = [] 
    for i in range(m): 
        column.append(matrix[i][j])
    transpose.append(column)  

print("Transpose of the matrix:")
for row in transpose:
    print(row)
