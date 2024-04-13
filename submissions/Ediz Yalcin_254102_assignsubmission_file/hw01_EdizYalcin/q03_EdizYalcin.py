matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None



transpose = []
rowsize = len(matrix[0])
colsize = len(matrix)

for n in range(rowsize):
    transpose.append([])
    
for i in range(rowsize):
    for j in range(colsize):
        transpose[i].append(matrix[j][i])
        
print(transpose)