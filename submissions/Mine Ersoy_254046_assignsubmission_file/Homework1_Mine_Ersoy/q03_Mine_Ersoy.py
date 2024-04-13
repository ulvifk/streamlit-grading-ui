matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

transpose_matrix = []
for i in range (len(matrix[0])):
    my_list = []
    for k in range(len(matrix)):
        my_list.append(matrix[k][i])
    transpose_matrix.append(my_list)
print(transpose_matrix)