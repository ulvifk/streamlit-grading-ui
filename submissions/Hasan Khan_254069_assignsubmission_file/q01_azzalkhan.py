my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"
words = my_string.split()
last_first_word = len(words) - 1 - words[::-1].index(words[-1])
remaining_words = len(words) - words.index(words[0])-1
different_words = len(set(words[:words.index(words[0])]))

print(f"The number of words to be read until the last word of the text is heard for the first time is {last_first_word}.")
print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")
print(f"The number of different words until we hear the first word for the last time is {different_words}.")
