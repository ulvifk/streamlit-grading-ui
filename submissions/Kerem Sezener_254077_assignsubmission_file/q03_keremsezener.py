matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None

num_rows: int = len(matrix)
num_columns: int = len(matrix[0])

transpose_num_rows = num_columns
transpose_num_columns = num_rows

transpose = []
for i in range(transpose_num_rows):
    transpose.append([])
    for j in range(transpose_num_columns):
        transpose[i].append(matrix[j][i])
        
print(transpose)