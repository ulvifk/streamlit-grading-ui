my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

all_words = my_string.split()

last_word=all_words[-1]
answer1 = all_words.index(last_word) + 1

first_word=all_words[0]
all_words_reversed = all_words[::-1]
answer2=all_words_reversed.index(first_word)

word_count = len(all_words)
unique_words=all_words[:word_count-all_words_reversed.index(first_word)]
answer3 = len(set(unique_words))


print("The number of words to be read until the last word of the text is heard for the first time is", answer1)
print("The number of remaining words after the first word is read for the last time is", answer2)
print("The number of different words until we hear the first word for the last time is", answer3)

