#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:02:47 2024

@author: batuhan
"""

my_dict = {}

for i in range(3,21):
    harmonic_num = 0
    count = 1
    while(harmonic_num <= i):
        harmonic_num += 1/count
        count += 1
    my_dict[i] = (count-1)
    
print(my_dict)


        
    

