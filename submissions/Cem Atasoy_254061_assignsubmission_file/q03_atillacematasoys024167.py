""""
soru3
"""

matrix = [[1, 2, 3], [4, 5, 6]]

tpose = None

tpose = []

for i in range(len(matrix[0])):
    
    row_tpose = []
    
    for row in matrix:

        row_tpose.append(row[i])
    
    tpose.append(row_tpose)

for row in tpose:
    print(row)
    
    