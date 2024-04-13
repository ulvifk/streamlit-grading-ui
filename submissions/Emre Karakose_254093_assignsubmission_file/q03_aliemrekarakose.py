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
col = len(matrix[0])

transpose = [[0 for _ in range(row)] for _ in range(col)]

for i in range(row):
    for j in range(col):
        transpose[j][i] = matrix[i][j]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)

