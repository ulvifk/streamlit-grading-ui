matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
transposed=[]
for i in range(0,len(matrix[0])):
    k=[]
    for a in range(0,len(matrix)):
        k.append(matrix[a][i])
    transposed.append(k)
print(transposed)
