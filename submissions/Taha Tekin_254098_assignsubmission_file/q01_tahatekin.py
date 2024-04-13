my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split()
last_word = words[-1]
first_word = words[0]

rule_1 = words.index(last_word) + 1

rule_2 = words[::-1].index(first_word)

last_word_index = len(words) - words[::-1].index(last_word) - 1
words_until_last_word = words[:last_word_index + 1]
rule_3 = len(set(words_until_last_word))

print(f"The number of words to be read until the last word of the text is heard for the first time is {rule_1}.")
print(f"The number of remaining words after the first word is read for the last time is {rule_2}.")
print(f"The number of different words until we hear the first word for the last time is {rule_3}.")