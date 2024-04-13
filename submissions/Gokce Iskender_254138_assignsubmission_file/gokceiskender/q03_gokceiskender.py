matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

def transpose_matrix(matrix):
   
    rows = len(matrix)
    columns = len(matrix[0])
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

    return transpose

transposed_matrix = transpose_matrix(matrix)

print(f"matrix = {matrix}")
print(f"transpose = {transposed_matrix}")
