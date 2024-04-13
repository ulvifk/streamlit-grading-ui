matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

matrix = [[1, 2, 3], [4, 5, 6]]


transpose = []


rows = len(matrix)
cols = len(matrix[0])


transpose = [[row[col] for row in matrix] for col in range(cols)]

print(transpose)



