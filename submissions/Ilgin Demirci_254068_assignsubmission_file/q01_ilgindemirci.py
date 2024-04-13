my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################



my_string = "in the end it is not the years in your life that count it is the life in your years"


words_list = my_string.split()


index_of_first_appearance_of_last_word = words_list.index(words_list[-1])


index_of_last_appearance_of_first_word = len(words_list) - words_list[::-1].index(words_list[0]) - 1


unique_words_until_last_appearance_of_first_word = len(set(words_list[0:index_of_last_appearance_of_first_word + 1]))


print(f"The number of words to be read until the last word of the text is heard for the first time is {index_of_first_appearance_of_last_word}.")
print(f"The number of remaining words after the first word is read for the last time is {len(words_list) - index_of_last_appearance_of_first_word - 1}.")
print(f"The number of different words until we hear the first word for the last time is {unique_words_until_last_appearance_of_first_word}.")