#q02



def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    transpose = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = transpose_matrix(matrix)
print("Transpose of the matrix:")
for row in transpose:
    print(row)
