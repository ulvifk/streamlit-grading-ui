matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
emty_set=[]

matrix1_row=len(matrix)
matrix1_collum=len(matrix[0])


for i in range(matrix1_collum):
    emty_set.append([])
    for j in range(matrix1_row):
        emty_set[i].append([0])


for i in range(matrix1_row):
    for j in range(matrix1_collum):
        emty_set[j][i]=matrix[i][j]
transpose=emty_set
print(transpose)
