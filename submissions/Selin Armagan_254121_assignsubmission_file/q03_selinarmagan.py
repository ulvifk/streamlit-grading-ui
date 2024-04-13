matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

n,p=len(matrix),len(matrix[0])
transpose=[[0]*n for i in range(p)]
x=0
y=0 
while (y<n):
    x=0
    while(x<p):
        transpose[x][y]=matrix[y][x]
        x+=1
    y+=1
print(transpose)