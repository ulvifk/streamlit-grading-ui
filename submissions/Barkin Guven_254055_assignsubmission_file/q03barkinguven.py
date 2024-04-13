
############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
"""start from here"""

matrix = [[1, 2, 3], [4, 5, 6]]
transpose = []
for i in range(len(matrix[0])):
    row=[]
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)
        