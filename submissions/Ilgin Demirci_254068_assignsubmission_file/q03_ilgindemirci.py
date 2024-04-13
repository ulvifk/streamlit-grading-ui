matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
row_count = len(matrix)
column_count = (len(matrix[0]))

for c in range (column_count):
    
    new_t_row = []
    
    for r in range (row_count):
        
        new_t_row.append(matrix[r][c])
        
    transpose.append(new_t_row)  
    
print(transpose)
 