matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

row=len(matrix)
col=len(matrix[0])
tranpose=[[matrix[j][i]] for j in range(row) for i in range(col)]
for row in tranpose:
    print(row)
