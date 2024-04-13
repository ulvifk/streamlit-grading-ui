


my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split(" ")
words_amount = len(words)


last_word = words[words_amount-1]
for i in range(words_amount):
    if words[i] == last_word:
        print("The number of words to be read until the last word of the text is heard for the first time (" + str(i+1) + ").")
        break

first_word = words[0]
first_word_last = 0
for i in range(words_amount):
    if words[i] == first_word:
        first_word_last = i + 1
print("The number of remaining words after the first word is read for the last time (" + str(words_amount-first_word_last) + ").")

different_words = []
for i in range(words_amount):
    if words[i] not in different_words:
        different_words.append(words[i])
print("The number of different words until we hear the first word for the last time (" + str(len(different_words)) + ").")