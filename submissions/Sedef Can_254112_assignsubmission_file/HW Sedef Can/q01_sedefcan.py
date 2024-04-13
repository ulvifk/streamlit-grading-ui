my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
list_x = []
list_x = my_string.split(" ")
set_x = set()

last_word = list_x[-1]
first_word = list_x[0]
list_x_len = len(list_x)

a = list_x.index(last_word)+1 
print(f"The number of words to be read until the last word of text is heard for the first time is {a}.")
b = list_x[::-1].index(first_word)
print(f"The number of remaining words after the first word is read for the last time is {b}.")

num_of_words_read = list_x_len - b

for i in range (num_of_words_read):
    d = list_x[i]
    set_x.add(d)
    
e = len(set_x)

print(f"The number of different words until we hear the first word for the last time is {e}.")    