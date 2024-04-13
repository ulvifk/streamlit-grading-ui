
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = None



rows=int(input("enter x:"))
cols=int(input("enter y:"))

matrix=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    matrix.append(col)

for i in range(rows):
    for j in range(cols):
        matrix[i][j]=int(input("Enter Value:"))
rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("\n")
for row in rez:
	print(row)
     
transpose = rez
print(transpose)