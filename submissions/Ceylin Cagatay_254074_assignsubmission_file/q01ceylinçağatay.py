my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"

# my_string = input("Please enter the string:")


words_list = my_string.split()

last_word = words_list[-1]


first_occurrence_index = words_list.index(last_word)
if first_occurrence_index == words_list[-1]:
    print("The last word of the test is unique")

print("The number of words to be read until the last word of the test is heard for the first time is {}.".format(first_occurrence_index + 1))

last_occurrence_index = len(words_list) - 1 - words_list[::-1].index(words_list[0])


remaining_words_count = len(words_list) - last_occurrence_index - 1
print("The number of remaining words after the first word is read for the last time is {}.".format(remaining_words_count))

last_occurrence_index = len(words_list) - 1 - words_list[::-1].index(words_list[0])


words_until_last_word_last_occurrence = set(words_list[:last_occurrence_index+1])


different_words_until_last_word_last_heard = len(words_until_last_word_last_occurrence)

print("The number of different words until we hear the first word for the last time is {}.".format(different_words_until_last_word_last_heard))