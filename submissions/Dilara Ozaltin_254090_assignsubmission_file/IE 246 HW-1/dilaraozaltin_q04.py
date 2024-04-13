#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:22:45 2024

@author: dilaraozaltin
"""

a=[]
i=1
while (i<=4):
    x=str(input(f"Enter choice {i}: "))
    x=int(x)
    if x not in range(0,10):
        print("Please choose a numeral from 0 to 9")
    elif (x in a):
        print("Please choose a different numeral at each time")
    else:
        a.append(x)
        i+=1
print(f"Your choices are {a}")