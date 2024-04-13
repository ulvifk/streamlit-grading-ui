# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:37:14 2024

@author: emreb
"""


my_string = "in the end it is not the years in your life that count it is the life in your years"

words = my_string.split()

first_occurrence = words.index(words[-1]) + 1

last_occurrence = len(words) - words[::-1].index(words[-1]) - 1

words_until_first_occurrence = first_occurrence

remaining_words_after_last_occurrence = len(words) - last_occurrence - 1

different_words_until_last_occurrence = len(set(words[:last_occurrence + 1]))

print(f"The number of words to be read until the last word of the text is heard for the first time is {words_until_first_occurrence}.")
print(f"The number of remaining words after the first word is read for the last time is {remaining_words_after_last_occurrence}.")
print(f"The number of different words until we hear the first word for the last time is {different_words_until_last_occurrence}.")






