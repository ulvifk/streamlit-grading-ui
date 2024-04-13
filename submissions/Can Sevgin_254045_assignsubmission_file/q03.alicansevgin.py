matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
m_list=[matrix[0],matrix[1]]
matrix =[[1,2,3],[4,5,6],]
matrix_transpose = []
for i in range(0,len(matrix[0])):
    transpose=[]
    for j in range(0,len(matrix)):
        transpose.append(matrix[j][i])
    matrix_transpose.append(transpose)
print(matrix_transpose) 
print(matrix)