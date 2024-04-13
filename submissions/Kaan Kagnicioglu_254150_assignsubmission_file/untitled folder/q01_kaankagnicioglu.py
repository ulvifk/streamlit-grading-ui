my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split()


total_words = len(words)
unique_words = set()
first_encounter = {}
last_encounter = {}

for i, word in enumerate(words):
    if word not in unique_words:
        unique_words.add(word)
    if word not in first_encounter:
        first_encounter[word] = i
    last_encounter[word] = i


words_until_last = last_encounter[words[-1]] + 1


remaining_words = total_words - first_encounter[words[0]]


different_words = len(unique_words)


print("Number of words to be read until the last word is heard for the first time:", words_until_last)
print("Number of remaining words after the first word is read for the last time:", remaining_words)
print("Number of different words until we hear the first word for the last time:", different_words)

 
