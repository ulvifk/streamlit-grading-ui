matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################



matrix = [[1,5,6,8],[2,5,9,7],[3,11,8,2]]


print( "The entered matrix is: ", matrix)

tp_matrix = []


for k in range(len(matrix[0])): 
    tp_row = []
    for i in range(len(matrix)):
        tp_row.append(matrix[i][k])
    tp_matrix.append(tp_row)
    
    
  

print( "Transpose of this matrix is: ", tp_matrix)


    
    

        
