my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = (my_string.split())

#1a
word_count = 0
for word in words:
    word_count += 1
    if word == words[-1]:
        break
        
print(f"The number of words to be read until the last word of the test is heard for the first time is {word_count}.")

#1b
remaining_words = 0
reversed_list = words[::-1]
for word in reversed_list:
    remaining_words += 1
    if word == words[0]:
        break
remaining_words -= 1
print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.") 




#1c
different_words = set()
count = 0
for word in words:
    different_words.add(word)
    
num_different = len(different_words)
print(f"The number of different words until we hear the first word for the last time is {num_different}.") 

     
    




