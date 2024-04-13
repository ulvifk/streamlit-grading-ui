# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:17:33 2024

@author: Lenovo
"""
matrix = [[1, 2, 3], [4, 5, 6]]
transpose=[]
count=0
count2=0
for i in matrix:
    count+=1
    for j in range(0,len(i)):
        count2+=1
count3=count2/count
for i in range(0,int(count3)):
    transpose.append([])
for a in range(0,len(transpose)):
    for b in range(0,len(matrix)):
        transpose[a].append(matrix[b][a])
print(transpose)       
