matrix = [[1, 2, 3], [4, 5, 6]]
transpose= None

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Wri]te your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
transpose=[]
row=len(matrix) 
column=len(matrix[0]) 

for j in range(column):
    transpose_list=[]
    transpose_list=[matrix[0][j]]
    for i in range(1,row):
        transpose_list.append(matrix[i][j])
    transpose.append(transpose_list)
print(transpose)
  