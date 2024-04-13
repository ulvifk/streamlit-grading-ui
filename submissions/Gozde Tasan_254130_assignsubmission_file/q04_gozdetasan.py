# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:22:23 2024

@author: asus
"""

submitted_numerals, i = [] , 1
while len(submitted_numerals) < 4:
    
    numeral = int(input(f"Enter choice {i}: "))
    
    if  numeral < 0 or numeral > 9:
        print("Please choose a numeral from 0 to 9.")
    else:
        if len(submitted_numerals) == 0:
            submitted_numerals.append(numeral)
            i += 1
        else:
            if numeral in submitted_numerals:
                print("Please choose a different numeral at each time.")
            else:
                submitted_numerals.append(numeral)
                i += 1
                
print(f"Your choices are {submitted_numerals}")    

        