#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:53:13 2024

@author: beratoner
"""




my_dict = {}

for i in range(3, 21):
    summ = 0
    n = 1
    list_of_n = []
    while summ < i:
        summ += 1/n
        list_of_n.append(n)
        n += 1
        if summ >= i:
            continue
    my_dict[i] = len(list_of_n)
print(my_dict)