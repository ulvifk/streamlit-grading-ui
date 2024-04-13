my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

#the number of words to be read until the last word of the text is heard for the first time:
    
words = my_string.split(" ")
last_word = words[-1]

first_index = words.index(last_word)

first_words = len(words[:(first_index+1)])

#the number of remaining words after the first word is read for the last time

word = words[0]
last_index = my_string.rfind(word)

my_index = last_index + len(word)
new_string = my_string[my_index+1:]
new_words = len(new_string.split(" "))


#the number of different words until we hear the first word for the last time 

different_words = len(set((my_string[:last_index]).split()))


print(f"""The number of words to be read until the last word of the test is heard for the first time is {first_words}.
The number of remaining words after the first word is read for the last time is {new_words}.
The number of different words until we hear the first word for the last time is {different_words}.""")























