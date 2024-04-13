#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:16:32 2024

@author: batuhan
"""

choice_num = 1
choices = []

while (choice_num <= 4):
    guess = int(input(f"Enter choice {choice_num}: "))
    if (guess<0 or guess>9):
        print("Please choose a numeral from 0 to 9.")
    elif (guess in choices):
        print("Please choose a different numeral at each time.")
    else:
        choice_num += 1
        choices.append(guess)

print(f"Your choices are {choices}.1")