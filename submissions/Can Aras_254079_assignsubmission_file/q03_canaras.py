matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################


transpose = []


for m in range(len(matrix[0])): 
    transpose_row = []
    for i in range(len(matrix)):
        transpose_row.append(matrix[i][m])
    transpose.append(transpose_row)
    
    
  

print( f"Transpose of this matrix is: {transpose}")
