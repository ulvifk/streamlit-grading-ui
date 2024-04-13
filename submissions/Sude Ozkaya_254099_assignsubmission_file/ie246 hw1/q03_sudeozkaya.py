matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

transpose=[]
row_length=len(matrix[0])
col_length=len(matrix)
for i in range(row_length):
    transpose.append([])
for j in range(row_length):
    for i in range(col_length):
        transpose[j].append(matrix[i][j])
print(transpose)