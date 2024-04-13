matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

m = len(matrix)
n = len(matrix[0])


transpose = []

for i in range(n):
    new_list = []
    for j in range(m):
        new_list.append(matrix[j][i])
    transpose.append(new_list)



print("Transpose: ", transpose)