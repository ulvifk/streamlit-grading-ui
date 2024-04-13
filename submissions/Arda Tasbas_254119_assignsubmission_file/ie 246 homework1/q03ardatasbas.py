matrix= [[1, 2, 3], [4, 5, 6]]
transpose_of_matrix = []

for i in range(len(matrix[0])):
    a=[]
    for j in range(len(matrix)):
        a.append(matrix[j][i])
    transpose_of_matrix.append(a)
        
print(transpose_of_matrix)