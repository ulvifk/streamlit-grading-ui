my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list = my_string.split()
last_word = my_list[-1] 
first_word = my_list[0]
a = my_list.index(last_word) + 1
print(f"The number of words to be read until the last word of the test is heard for the first time is {a}.")

b = my_list[::-1].index(first_word)
print(f"The number of remaining words after the first word is read for the last time is {b}.")

my_set = set()
numberofwords = len(my_list) - b
for i in range(numberofwords):
    d = my_list[i]
    my_set.add(d)
print(f"The number of different words until we hear the first word for the last time is {len(my_set)}.")