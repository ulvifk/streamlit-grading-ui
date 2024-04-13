matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

matrix = [[1, 2, 3], 
          [4, 5, 6]]
transpose = []

row = len(matrix)
col = len(matrix[0])

for i in range(col):
    transpose_row = []
    
    for j in range(row):
        transpose_row.append(matrix[j][i])
    transpose.append(transpose_row)  
print(transpose)
