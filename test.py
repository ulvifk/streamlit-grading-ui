
matrix = [[3, 2, 5], [1, 3, 5]]
transpose = []
m, n = len(matrix), len(matrix[0])
for j in range(n):
    transpose.append([])
    for i in range(m):
        transpose[j].append(matrix[i][j])
print(transpose)