matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

############################################################################
# Do not change the code above.
# Above code will be used in testing your script.
# Write your script down below.
# You are expected to calculate the transpose of the given matrix, and assign 
#     it to the variable 'transpose'.
############################################################################

# (1,2,3)
# (4,5,6)

result_list = []
mid_list = []

for i in range(len(matrix[0])):
    for j in matrix:
        mid_list.append(j[i])
    result_list.append(mid_list)
    mid_list = []
transpose = result_list
print(transpose)


        
        
        
                   
                        