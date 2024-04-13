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

transposedMatrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(n):
        transposedMatrix[j][i] = matrix[i][j]
        
print("Original Matrix is as following:")
for row in matrix:
    print(row)

print("Transposed Matrix is as following:")
for row in transposedMatrix:
    print(row)        