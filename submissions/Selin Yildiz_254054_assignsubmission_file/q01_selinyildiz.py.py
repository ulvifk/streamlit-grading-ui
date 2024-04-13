my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_words = my_string.split()
 
last_word = my_words[-1]
last_word_first = my_words.index(last_word) + 1
print(f"The number of words to be read until the last word of the test is heard for the first time is {last_word_first}.")


first_word = my_words[0]
remaining_words = my_words[::-1].index(first_word)
print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")


first_word_last = len(my_words)- my_words[::-1].index(first_word)
different_words = len(set(my_words[:first_word_last]))
print(f"The number of different words until we hear the first word for the last time is {different_words}.")
