matrix = [[1, 2, 3], [4, 5, 6]]
transpose = []

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

num_cols = len(matrix[0])
num_rows = len(matrix)

for i in range(num_cols):
    row=[]
    for j in range(num_rows):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)

