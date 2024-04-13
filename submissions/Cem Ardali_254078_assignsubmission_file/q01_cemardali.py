

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"

words = my_string.split()

words_until_last = words.index(words[-1]) + 1

print(f"The number of words to be read until the last word of the text is heard for the first {words_until_last}.")


first_word_index = len(words) - words[::-1].index(words[0]) - 1

words_until_last = words[:first_word_index + 1]

remaining_words = (len(words)- len(words_until_last))

print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")


first_word_index = len(words) - words[::-1].index(words[0]) - 1

words_until_last = words[:first_word_index + 1]

diff_words_until_last = len(set(words_until_last))


print(f"The number of different words until we hear the first word for the last time is {diff_words_until_last}.")