# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:16:50 2023

@author: kaan
"""

my_string = "in the end it is not the years in your life that count it is the life in your years"
words=my_string.split(" ")

last_word_first_index=words.index(words[-1])
words_rev=words[-1::-1]
first_word_last_time=words_rev.index(words[0])  

a=int(last_word_first_index)+1
b=first_word_last_time
unique_words = set()
count=0
for word in words:
        if word in unique_words:
            break
unique_words.add(word)  
count += 1
c=count 
print(f"""The number of words to be read until the last word of the test is heard for the first time is {a}.
The number of remaining words after the first word is read for the last time is {b}. The number
of different words until we hear the first word for the last time is {c}.""")
