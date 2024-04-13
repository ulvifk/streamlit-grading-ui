# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:46:16 2024

@author: Lenovo
"""
mydict={i:0 for i in range(3,21)}
for i in mydict.keys():
    j=1
    while True:
        mydict[i] += 1/j
        j +=1
        if mydict[i]>i:
            break
        
        
        
print(mydict)


