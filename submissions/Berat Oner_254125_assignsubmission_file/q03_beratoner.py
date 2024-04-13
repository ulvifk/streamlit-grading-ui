#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:22:22 2024

@author: beratoner
"""

matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[1, 4], [2, 5], [3, 6]]

nrow = len(matrix)
ncol = len(matrix[0])

new_transpose = []

for i in range(ncol): #ncol = 3
    temp = []
    for j in range(nrow): #nrow = 2
        temp.append(matrix[j][i])
    new_transpose.append(temp)

print(new_transpose)