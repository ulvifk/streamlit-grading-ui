matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################


columns=len(matrix[0])
rows=len(matrix)
j=0
i=0
transpose=[]


for i in range(len(matrix[0])):
    transpose_row=[]
    for j in range (len(matrix)):
        transpose_row.append(matrix[j][i])
    transpose.append(transpose_row)
        
print(transpose)