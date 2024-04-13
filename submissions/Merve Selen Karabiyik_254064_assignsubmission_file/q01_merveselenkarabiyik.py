my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################



words = my_string.split()


word_count = {}


for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1


last_word_index = len(words) - 1 - words[::-1].index(words[-1])


first_occurrence_last_word = words.index(words[-1])


last_occurrence_first_word = last_word_index - words[::-1].index(words[0])


words_until_last_word_first_time = first_occurrence_last_word + 1


remaining_words_after_first_word_last_time = len(words) - last_occurrence_first_word - 1


different_words_until_first_word_last_time = len(set(words[:first_occurrence_last_word + 1]))

print("The number of words to be read until the last word of the text is heard for the first time is {}.".format(words_until_last_word_first_time))
print("The number of remaining words after the first word is read for the last time is {}.".format(remaining_words_after_first_word_last_time))
print("The number of different words until we hear the first word for the last time is {}.".format(different_words_until_first_word_last_time))
