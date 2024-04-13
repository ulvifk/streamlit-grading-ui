#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:22:10 2024

@author: dilaraozaltin
"""


result={}
for number in range(3,20):
    sayac=0
    sum=0
    
    for i in range (1,9999999):
        sum=sum+(1/i)
        sayac+=1
        if (sum>=number ):
            result[number]=sayac
            break
        else:
            continue
print(result)
    