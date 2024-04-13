matrix= [[1, 2, 3], [4, 5, 6]]
transpose = []

for i in range(len(matrix[0])):
    a=[]
    for j in range(len(matrix)):
        a.append(matrix[j][i])
    transpose.append(a)
        
print(transpose)