# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:08:47 2024

@author: emreb
"""

chosen_numbers = []

while len(chosen_numbers) < 4:
    user_input = input(f"Enter choice {len(chosen_numbers) + 1}: ")
    try:
        choice = int(user_input)
        if choice < 0 or choice > 9:
            print("Please choose a numeral from 0 to 9.")
        elif choice in chosen_numbers:
            print("Please choose a different numeral at each time.")
        else:
            chosen_numbers.append(choice)
    except ValueError:
        print("Please enter a valid integer.")

print(f"Your choices are {chosen_numbers}.")



