# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:59:27 2024

@author: Emir Gencay
"""

matrix = [[1, 2, 3], [4, 5, 6]]
transpose=None
transpose=[]
for i in range(len(matrix[0])):
    row=[]
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)
        




