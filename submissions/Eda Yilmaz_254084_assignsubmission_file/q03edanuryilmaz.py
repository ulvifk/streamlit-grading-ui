matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

n=len(matrix)
p=len(matrix[0])

#creates an initial transpose list with values of 0 for each index

transpose = [[0]*n for _ in range(p)]

b=0
c=0

#changes the 0 values into the rows and columns by adding 1 to each index

while (c<n):
    b=0
    while(b<p):
        transpose[b][c]=matrix[c][b]
        b=b+1
    c=c+1

print(transpose)

    
    