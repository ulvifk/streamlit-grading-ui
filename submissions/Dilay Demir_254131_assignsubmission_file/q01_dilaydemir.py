my_string="in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
string_list=my_string.split()
last_word=string_list[-1]
index_last_word=string_list.index(last_word)
print(f"The number of words to be read until the last word of the test is heard for the first time is {index_last_word+1}.")

reverse_string=string_list[::-1]
first_word=string_list[0]
index_first_word=reverse_string.index(first_word)
print(f"The number of remaining words after the first word is read for the last time is {index_first_word}.")

del reverse_string[0:index_first_word]
for word in reverse_string:
    if reverse_string.count(word)>1:
        reverse_string.remove(word)
        different=len(reverse_string)
print(f"The number of different words until we hear the first word for the last time is {different}.")


