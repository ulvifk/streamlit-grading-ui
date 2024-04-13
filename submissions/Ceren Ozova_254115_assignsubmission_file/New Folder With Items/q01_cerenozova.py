my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def calculate_word_statistics(text):
    words = text.split()
    last_word = words[-1]
    first_occurrence_index = words.index(last_word)
    
    num_words_until_last_word_first_time = first_occurrence_index + 1
    num_remaining_words_after_last_word_first_time = len(words) - first_occurrence_index - 1
    unique_words_until_last_word_last_time = len(set(words[:first_occurrence_index]))

    print(f"The number of words to be read until the last word of the text is heard for the first time is {num_words_until_last_word_first_time}.")
    print(f"The number of remaining words after the first word is read for the last time is {num_remaining_words_after_last_word_first_time}.")
    print(f"The number of different words until we hear the first word for the last time is {unique_words_until_last_word_last_time}.")