my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split()
last=words[-1]
last_word = words.index(last) +1
first=words[0]
first_word = len(words) - words[::-1].index(first) -1
remaining_words = len(words) - first_word -1
unique = len(set(words[:first_word + 1]))

print(f"The number of words to be read until the last word of the text is heard for the first time is {last_word}.")

print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")

print(f"The number of different words until we hear the first word for the last time is {unique}.")