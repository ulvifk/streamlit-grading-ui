my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def calculate_word_counts(text):
    words = text.split()  
    unique_words = set()  
    last_index = {}  
    first_index = {} 

    for i, word in enumerate(words):
        unique_words.add(word)  
        last_index[word] = i 
        if word not in first_index:
            first_index[word] = i

    last_word = words[-1] 
    words_until_last_word = last_index[last_word] + 1  
    remaining_words = len(words) - last_index[last_word] - 1 
    unique_words_until_last_word = len(unique_words) - (len(words) - words_until_last_word)  

    output1 = f"The number of words to be read until the last word of the text is heard for the first time is {words_until_last_word}'dir."
    output2 = f"The number of remaining words after the first word is read for the last time is {remaining_words}'dir."
    output3 = f"The number of different words until we hear the first word for the last time is {unique_words_until_last_word}'dir."

    print(output1)
    print(output2)
    print(output3)

my_string = "in the end it is not the years in your life that count it is the life in your years"
calculate_word_counts(my_string)