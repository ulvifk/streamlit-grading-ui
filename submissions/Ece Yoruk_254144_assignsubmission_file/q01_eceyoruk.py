my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################



  
words=my_string.split()   


until_last_word_first_occurance=words.index(words[-1]) + 1

print(f"The number of words to be read until the last word of the test is heard for the first time is {until_last_word_first_occurance}")



remaining_after_first_words_last_occurance=words[::-1].index(words[0])

print(f"The number of remaining words after the first word is read for the last time is {remaining_after_first_words_last_occurance}")



different_words=set()

for word in words[:(len(words)-remaining_after_first_words_last_occurance)]:
    if word not in different_words:
        different_words.add(word)
    
print(f"The number of different words until we hear the first word for the last time is {len(different_words)}")