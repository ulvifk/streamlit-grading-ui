my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


my_array = my_string.split(" ")
last_word = my_array[len(my_array)-1]
first_word = my_array[0]
reverse_list = my_array.copy()
reverse_list.reverse()
first_half = my_array.copy()
first_half = first_half[:(len(my_array)+1)//2]
second_half = my_array.copy()
second_half = second_half[(len(my_array)+1)//2:len(my_array)]
my_set = set(my_string)
my_set.remove(' ')
my_list = list(my_set)
my_list.sort()
first = my_array.index(last_word)+1
second = reverse_list.index(first_word)
third = len(set(my_array[:len(my_array)-reverse_list.index(my_array[0])-1]))
fourth = len(set(first_half).intersection(set(second_half)))
fifth = my_list[round((len(my_list)-1)/2)].upper()
print("The number of words to be read until the last of the test is heard for the first time is", first)
print("The number of remaining words after the first word is read for the last time is", second)
print("The number of different words until we hear the first word for the last time is", third)
print("The number of common words used in the first and the second half of the text is", fourth)
print("The letter which seperates the first approximate half of the used words from the second approximate half when all words that have been used are sorted alphabetically is", fifth)


