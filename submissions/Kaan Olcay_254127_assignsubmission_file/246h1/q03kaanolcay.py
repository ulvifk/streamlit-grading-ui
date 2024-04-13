matrix= [[1, 2, 3], [4, 5, 6]]
transpose = []

for i in range(len(matrix[0])):
    k=[]
    for j in range(len(matrix)):
        k.append(matrix[j][i])
    transpose.append(k)
        
print(transpose)