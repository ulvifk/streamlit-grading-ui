#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:38:16 2024

@author: aleynasuaktas
"""
def get_lottery_choices():
    choices = []

    while len(choices) < 4:
        choice = input("Enter choice {}: ".format(len(choices) + 1))

        
        if not choice.isdigit():
            print("Please enter a valid numeral.")
            continue

        choice = int(choice)

 
        if choice < 0 or choice > 9:
            print("Please choose a numeral from 0 to 9.")
            continue

  
        if choice in choices:
            print("Please choose a different numeral at each time.")
            continue

        choices.append(choice)

    return choices


def main():
    print("Please choose 4 different numerals from 0 to 9.")

    
    lottery_choices = get_lottery_choices()

    print("Your choices are {}.".format(lottery_choices))

if __name__ == "__main__":
    main()
