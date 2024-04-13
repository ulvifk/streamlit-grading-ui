my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"

str_list = my_string.split() #splitting text for " " and turning into list
print(str_list)

last = str_list[-1] # last word of the list

index_last = str_list.index(last) # index number of last word


reverse_str = str_list[::-1] # reversing the list

first = str_list[0] # "in"

index_first = reverse_str.index(first) # index number of "in"


for word in reverse_str:
    
    if reverse_str.count(word) > 1:
        reverse_str.remove(word)
        different = len(reverse_str)
print(f"""The number of words to be read until the last word of the test is heard for the first time is {index_last+1}.
      The number of different words until we hear the first word for the last time is {different}.
      The number of remaining words after the first word is read for the last time is {index_first}.""")