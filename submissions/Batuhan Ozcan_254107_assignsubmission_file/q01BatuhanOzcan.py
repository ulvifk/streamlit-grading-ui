my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = my_string.split()
last_word = my_string[-1]

# Count occurrences of each word
word_counts = {}
for word in my_string:
    word_counts[word] = word_counts.get(word, 0) + 1

# Calculate the number of words until the last word is heard for the first time
words_until_last_word = my_string.index(last_word) + 1

# Calculate the number of remaining words after the first word is read for the last time
remaining_words = len(my_string) - my_string[::-1].index(last_word) - 1

# Calculate the number of different words until we hear the first word for the last time
different_words = len(word_counts)

# Print the results
print(f"The number of words to be read until the last word of the text is heard for the first time is {words_until_last_word}.")
print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")
print(f"The number of different words until we hear the first word for the last time is {different_words}.")