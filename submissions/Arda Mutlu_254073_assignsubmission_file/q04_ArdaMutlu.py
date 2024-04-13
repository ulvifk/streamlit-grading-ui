# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:57:55 2024

@author: Lenovo
"""
secilenler=[]
count=1
while count<=4:
    sayi=int(input(f"Enter choice {count}:"))
    if (sayi<=9) and (sayi>=0):
        if sayi in secilenler:
            print("Please choose a different numeral at each time.")
        else:
            secilenler.append(sayi)
            count+=1
    else:
        print("Please choose a numeral from 0 to 9")
print(f"Your choices are{secilenler}")

    
    