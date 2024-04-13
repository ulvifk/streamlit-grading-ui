#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:28:07 2024

@author: aleynasuaktas
"""

def calculate_word_stats(text):
    words = text.split()
    word_count = len(words)

  
    word_occurrences = {}

    for word in words:
        if word not in word_occurrences:
            word_occurrences[word] = 1
        else:
            word_occurrences[word] += 1

   
    first_occurrence_count = 0
    for word in words:
        first_occurrence_count += 1
        if word_occurrences[word] == 1:
            break

 
    last_occurrence_count = 0
    for word in reversed(words):
        last_occurrence_count += 1
        if word_occurrences[word] == 1:
            break

    distinct_words_count = len(word_occurrences)
    print("The number of words to be read until the last word of the text is heard for the first time is {}.".format(first_occurrence_count))
    print("The number of remaining words after the first word is read for the last time is {}.".format(last_occurrence_count))
    print("The number of different words until we hear the first word for the last time is {}.".format(distinct_words_count))

my_string = "in the end it is not the years in your life that count it is the life in your years"
calculate_word_stats(my_string)
