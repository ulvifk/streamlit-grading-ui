matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

row = len(matrix)
column = len(matrix[0])
transpose = []

for i in range(column):
    temp = []
    temp.append(0)
    transpose.append(row*temp)
print(transpose)

for i in range(row):
    for j in range(column):
        transpose[j][i] = matrix[i][j]
print(transpose)