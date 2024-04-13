#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:22:34 2024

@author: dilaraozaltin
"""

original_matrix = [[3, 2, 4, 5, 5], [4, 5, 2, 4, 6], [1, 4, 2, 5, 1, 2]]
transposed_matrix = []

for i in range(len(original_matrix[0])):
    new_column = []

    for row in original_matrix:
        new_column.append(row[i])
    transposed_matrix.append(new_column)

print(f"The original matrix is: {original_matrix}")
print(f"The transposed matrix is: {transposed_matrix}")