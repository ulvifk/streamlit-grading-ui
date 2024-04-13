# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:22:13 2024

@author: asus
"""

matrix = [[1, 2, 3], [4, 5, 6]]

num_rows = len(matrix)
num_cols = len(matrix[0])

transpose = [[0 for j in range(num_rows)] for i in range(num_cols)]

for i in range(num_rows):
    for j in range(num_cols):
        transpose[j][i] = matrix[i][j]

print(transpose)
