# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:01:19 2024

@author: emreb
"""


matrix = [[1, 2, 3], [4, 5, 6]]

transpose = []

num_rows = len(matrix)
num_cols = len(matrix[0])

for i in range(num_cols): 
    transpose.append([])
    for j in range(num_rows): 
        transpose[i].append(matrix[j][i])

print(transpose)








