# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:22:27 2024

@author: Emir Gencay
"""


choices=[]
lencho=len((choices))

while lencho<4:
    x=input(f"Enter choice {lencho+1}:")
    try:
        x = int(x)
        if x>=0 and x<=9:
            if x not in choices:
                choices.append(x)
                lencho+=1
            else:
                print("Please choose a different numeral at each time.")
        else:
            print("Please choose a numeral from 0 to 9.")
    except :
        print("Invalid input. Please enter a numeral.")

print(f"Your choices are {choices}")
