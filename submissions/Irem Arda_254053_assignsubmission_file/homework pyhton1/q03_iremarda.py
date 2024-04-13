matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

transpose=[]
for i in range(0,len(matrix[0])):
    t=[]
    for j in range(0,len(matrix)):
        t.append(matrix[j][i])
    transpose.append(t)
    print(f'This matrix tranpose is {transpose}.')
    