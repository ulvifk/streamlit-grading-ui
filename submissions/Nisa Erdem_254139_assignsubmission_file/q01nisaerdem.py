my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def calculate_values(text):
    words = text.split()
    total_words = len(words)string'
    last_index_of_first_word = len(words) - 1 - words[::-1].index(words[0])
    

    words_until_last_word_first_time = last_index_of_first_word + 1
    
    
    remaining_words = total_words - last_index_of_first_word - 1
    
    # Number of different words until we hear the first word for the last time
    different_words_until_last_word = len(set(words[:last_index_of_first_word + 1]))
    
    return words_until_last_word_first_time, remaining_words, different_words_until_last_word

# Example string
my_string = "in the end it is not the years in your life that count it is the life in your years"

# Calculate values
words_until_last_word_first_time, remaining_words, different_words_until_last_word = calculate_values(my_string)

# Print the results
print("The number of words to be read until the last word of the text is heard for the first time is {}.".format(words_until_last_word_first_time))
print("The number of remaining words after the first word is read for the last time is {}.".format(remaining_words))
print("The number of different words until we hear the first word for the last time is {}.".format(different_words_until_last_word))
