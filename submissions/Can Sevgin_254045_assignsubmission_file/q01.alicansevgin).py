my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = my_string.split()
last_w = my_string[-1]

counts = {}
for word in my_string:
    counts[word] = counts.get(word, 0) + 1

total_words = my_string.index(last_w) + 1
remaining_word= len(my_string) - my_string[::-1].index(last_w) - 18
different_word = len(counts)

print(f"The number of words to be read until the last word of the text is heard for the first time is {total_words}.")
print(f"The number of remaining words after the first word is read for the last time is {remaining_word}.")
print(f"The number of different words until we hear the first word for the last time is {different_word}.")
