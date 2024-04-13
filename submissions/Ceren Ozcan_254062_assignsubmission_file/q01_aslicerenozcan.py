my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

listem = my_string.split()

first_time= listem.index(listem[-1]) + 1

print("The number of words to be read until the last word of the test is heard for the first time is:", first_time)

#question 1 part 2

listem_2=my_string.split()

listem_2.reverse()

aklimda= listem_2.index(listem[0])

remaining_words= len(listem)-(len(listem)-aklimda)

print("The number of remaining words after the first word is read for the last time is:", remaining_words)

#question 1 part 3

normal_index = len(listem)-aklimda-1

frozen_set= frozenset(listem[:normal_index])

print(" The number of different words until we hear the first word for the last time is: ", len(frozen_set))

