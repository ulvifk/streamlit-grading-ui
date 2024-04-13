# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:21:55 2024

@author: asus
"""

k_vals = {i:0 for i in range(3,21)}
summation = 0
n = 1
for k in k_vals:
    while summation <= k:
        summation += 1/n
        n += 1
    k_vals[k] = n
    
print(k_vals)
