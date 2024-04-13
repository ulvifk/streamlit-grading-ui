my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"

words = my_string.split()
last_word = words.index(words[-1]) + 1
print(f"the number of words to be read until the last word of the test is heard for the first time is {last_word}")

first_word = len(words) - words[::-1].index(words[0])
remaining = len(words) - first_word
print(f"the number of remaining words after the first word is read for the last time is {remaining}")

different_words = len(set(words[:first_word]))
print(f"the number of different words until we hear the first word for the last time is {different_words}")


