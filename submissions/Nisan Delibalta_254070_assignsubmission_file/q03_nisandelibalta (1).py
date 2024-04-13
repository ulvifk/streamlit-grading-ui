matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

rows = len(matrix)
columns = len(matrix[0])

transpose = [[] for _ in range(columns)]


for i in range(rows):
    for j in range(columns):
        transpose[j].append(matrix[i][j])
        
        
for row in transpose:
    print(row)
