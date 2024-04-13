my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

string_list = my_string.split( )
counter = 0
counter2 = 2
for word in string_list:
    counter += 1 
    if string_list[-1] == word and counter != len(string_list):
        print(f"The number of words to be read until the last word of the text is heard for the first time is {counter}.")

counter = 0
for word in string_list:
    counter += 1
    if string_list[0] == word:
        counter2 = counter
print(f"The number of remaining words after the first word is read for the last time is {counter - counter2}.")

string_set = set()
counter = 0
for word in string_list:
    counter += 1
    if string_list[0] == word:
        counter2 = counter
for word in range(0,counter2):
    string_set.add(string_list[word])
print(f"The number of different words until we hear the first word for the last time is {len(string_set)}.")