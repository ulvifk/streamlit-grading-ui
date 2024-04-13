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
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if i == 0:
            transpose = [[matrix[i][j]] for j in range(cols)]
        else:
            transpose[j].append(matrix[i][j])

print(matrix)
print(transpose)



