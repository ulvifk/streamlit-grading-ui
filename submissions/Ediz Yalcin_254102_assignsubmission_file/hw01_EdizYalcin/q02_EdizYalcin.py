#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:35:47 2024

@author: edizyalcin
"""
harmonic_series_dict = {}
for n in range(3, 21): #The code works but takes too long to give an answer in this range, when the range is decreased, it prints out the answer
    sum = 1.0
    terms = 1.0
    while sum < n:
        terms += 1
        sum += 1.0 / terms
        
                  
        
    harmonic_series_dict[n] = terms
        

print(harmonic_series_dict)