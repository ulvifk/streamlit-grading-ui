# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:15:31 2023

@author: kaan
"""

choices = []

for i in range(1, 5):
    while True:
            choice = int(input(f"Enter choice {i}: "))

            if 0 <= choice <= 9 and choice not in choices:
                    choices.append(choice)
                    break
            elif choice in choices:
                    print("Please choose a different numeral at each time.")
            else:
                    print("Please choose a numeral from 0 to 9.")
print(f"Your choices are: {choices}.")
            