# Question 3 - Elif Sırma Ceylan

matrix =  [[1, 2, 3],
           [4, 5, 6]]


transpose=[]

column=len(matrix[0])
row=len(matrix)

for i in range(column):

    transpose.append([])
	
    for j in range(row):
	
        a=matrix[j][i]
        transpose[i].append(a)

print(transpose)

