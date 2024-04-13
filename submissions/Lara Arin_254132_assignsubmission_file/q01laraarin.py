my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split()
word_num = {word: words.index(word) for word in set(words)}

first_words = {word: words.index(word) for word in set(words)}
last_words = {word: len(words) - 1 - words[::-1].index(word) for word in set(words)}

section_a = first_words[words[-1]] + 1
section_b = len(words) - last_words[words[0]]
section_c = len(set(words[:section_a]))

print(f"The number of words to be read until the last word of the text is heard for the first time is : {section_a}.")
print(f"The number of remaining words after the first word is read for the last time is : {section_b}.")
print(f"The number of different words until we hear the first word for the last time is : {section_c}.")
