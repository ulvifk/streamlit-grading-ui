#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:35:56 2024

@author: aleynasuaktas
"""

def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    transpose = [[None]*num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
