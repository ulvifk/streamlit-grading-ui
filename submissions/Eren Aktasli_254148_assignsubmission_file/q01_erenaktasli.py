my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def calculate_word_stats(input_string):
    words = input_string.split()
    total_words = len(words)
    
    
    first_occurrence = {}
    for i, word in enumerate(words):
        if word not in first_occurrence:
            first_occurrence[word] = i
    words_until_first_last_word = first_occurrence[words[-1]] + 1
    
    
    last_occurrence = {}
    for i, word in enumerate(reversed(words)):
        if word not in last_occurrence:
            last_occurrence[word] = i
    remaining_words_after_first_last_word = last_occurrence[words[0]] 
    
    
    last_word_index = total_words - 1 - words[::-1].index(words[-1])
    unique_words_until_last_word = len(set(words[:last_word_index+1]))
    
    
    print(f"The number of words to be read until the last word of the text is heard for the first time is {words_until_first_last_word}.")
    print(f"The number of remaining words after the first word is read for the last time is {remaining_words_after_first_last_word}.")
    print(f"The number of different words until we hear the first word for the last time is {unique_words_until_last_word}.")


calculate_word_stats(my_string)