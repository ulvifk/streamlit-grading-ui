my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words_in_string = my_string.split(" ")

first_seeing_i = -1
last_seeing_i = -1


for i in range(len(words_in_string)):
    if ((words_in_string[i] == words_in_string[-1]) and (first_seeing_i == -1)):
        first_seeing_i = i
        
    if (words_in_string[i] == words_in_string[0]):
        last_seeing_i = i

if (first_seeing_i != -1):
    last_word = first_seeing_i + 1
    remaining_words = len(words_in_string) - (last_seeing_i + 1)

    
before_last = len(set(words_in_string))
    
print(f'The number of words to be read until the last word of the text is heard for the first time: {last_word}')
print(f'The number of remaining words after the first word is read for the last time: {remaining_words}')
print(f'The number of different words until we hear the first word for the last time: {before_last}')
       
