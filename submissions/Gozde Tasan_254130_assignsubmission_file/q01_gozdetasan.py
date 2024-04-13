# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:21:38 2024

@author: asus
"""

my_string = "in the end it is not the years in your life that count it is the life in your years"
st_list = my_string.split()

last_word = st_list[-1]
first_word = st_list[0]

last_word_first_occurence = st_list.index(last_word)
remaining_words_count = len(st_list[:last_word_first_occurence+1])
print(f"The number of words to be read until the last word of the test is heard for the first time is {remaining_words_count}.")

first_word_last_occurence = st_list[::-1].index(first_word)
print(f"The number of remaining words after the first word is read for the last time is {first_word_last_occurence}.")

unique_words_until_last_occurence = len(set(st_list[:len(st_list)-first_word_last_occurence-1]))

print(f"The number of different words until we hear the first word for the last time is {unique_words_until_last_occurence}.")
