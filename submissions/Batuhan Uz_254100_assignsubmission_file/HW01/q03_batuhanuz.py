#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:10:07 2024

@author: batuhan
"""

matrix = [[1, 2, 3], [4, 5, 6]]
transpose = []

for i in range(len(matrix[0])):
    arr=[]
    for j in range(len(matrix)):
        arr.append(matrix[j][i])
    transpose.append(arr)
        
print(transpose)