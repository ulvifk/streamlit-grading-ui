matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
transpose = []
x = len(matrix[0])
y = len(matrix)

for i in range(x):
    transpose.append([])
    
for j in range(x):
    for i in range(y):
        transpose[j].append(matrix[i][j])
    
    
print(transpose)