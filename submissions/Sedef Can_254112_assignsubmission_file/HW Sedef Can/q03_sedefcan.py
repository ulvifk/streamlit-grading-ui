matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

a = len(matrix)
b = len(matrix[0])

transpose = [[0]*a for i in range(b)]

c = 0 
d = 0

while (d < a):
    c = 0
    while (c < b):
        transpose[c][d] = matrix[d][c]
        c = c + 1
    d = d + 1
    
print(transpose)
