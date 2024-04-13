matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################
newMatrix=[]
for x in range(0,len(matrix[0])):
    mylist=[]
    for y in range(0,len(matrix)):
        mylist.append(matrix[y][x])
    newMatrix.append(mylist)
        
print(newMatrix)
        
        
        
       
        
        




