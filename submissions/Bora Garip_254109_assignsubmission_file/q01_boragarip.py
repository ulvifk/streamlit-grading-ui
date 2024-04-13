my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def calculate_word_counts(text):
    words = text.split()
    unique_words = set(words)
    word_count = len(words)
    unique_word_count = len(unique_words)

   
    last_index_of_first_word = len(words) - 1 - words[::-1].index(words[0])

    words_until_last_occurrence_of_first_word = last_index_of_first_word + 1
    remaining_words_after_last_occurrence_of_first_word = word_count - last_index_of_first_word - 1

    return (words_until_last_occurrence_of_first_word, remaining_words_after_last_occurrence_of_first_word, unique_word_count)

my_string = "in the end it is not the years in your life that count it is the life in your years"

word_counts = calculate_word_counts(my_string)

print("The number of words to be read until the last word of the text is heard for the first time is {}.".format(word_counts[0]))
print("The number of remaining words after the first word is read for the last time is {}.".format(word_counts[1]))
print("The number of different words until we hear the first word for the last time is {}.".format(word_counts[2]))