def word_count(my_string):

    my_array = my_string.split(" ")
    last_word = my_array[len(my_array)-1]
    first_word = my_array[0]
    reverse_list = my_array.copy()
    reverse_list.reverse()
    first = my_array.index(last_word)+1
    second = reverse_list.index(first_word)
    third = len(set(my_array[:len(my_array)-reverse_list.index(my_array[0])-1]))

    print("The number of words to be read until the last of the test is heard for the first time is", first)
    print("The number of remaining words after the first word is read for the last time is", second)
    print("The number of different words until we hear the first word for the last time is", third)
my_string = "in the end it is not the years in your life that count it is the life in your years"
word_count(my_string)












############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

 