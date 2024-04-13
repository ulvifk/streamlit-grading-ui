my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


splitted = my_string.split()

last_first = splitted[::1].index(splitted[-1]) + 1

first_last = splitted[::-1].index(splitted[0])

new_list = list() 
for i in splitted:
    if i not in new_list:
        new_list.append(i)
        len_of_new_list = len(new_list)
        

text = f"The number of words to be read until the last word of the test is heard for the first time is {last_first}."
text += f"The number of remaining words after the first word is read for the last time is {first_last}."
text += f"The number of different words until we hear the first word for the last time is {len_of_new_list}."
print(text)