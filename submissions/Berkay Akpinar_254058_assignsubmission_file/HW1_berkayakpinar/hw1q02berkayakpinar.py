# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:54:48 2024

@author: emreb
"""


results = {}

for k in range(3, 21):
    total = 0
    terms = 0
    while total < k:
        terms += 1
        total += 1 / terms
    results[k] = terms

print("Minimum number of terms needed to be added up in the finite harmonic series:")

print(results)










