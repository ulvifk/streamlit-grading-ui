#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:40:23 2024

@author: beratoner
"""

choices_list = []
i = 1

while len(choices_list) < 4:
    choice = int(input(f"Enter choice {i}: "))
    if choice >= 0 and choice <= 9:
        if choice not in choices_list:
            choices_list.append(choice)
            i += 1
        else:
            print("Please choose a different numeral at each time. ")
    else:
        print("Please choose a numeral from 0 to 9")
        
print(choices_list)