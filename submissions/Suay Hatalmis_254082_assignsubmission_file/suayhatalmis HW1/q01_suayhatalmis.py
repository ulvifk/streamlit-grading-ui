my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


my_list = list(my_string.split(" "))

x = my_list.index(my_list[-1])

# it says "until" the last word is heard,
# there are 7 words until the word 'years' is first heard
# how can it be 8?

liste = my_list[:]
liste.reverse()
k = liste.index(my_list[0])

y = k



my_list2= []
for i in liste[k:]:
    if i not in my_list2:
        my_list2.append(i)
z = len(my_list2)




print(f"The number of words to be read until the last word of the text is heard for the first time is {x}")
print(f"The number of remaining words after the first word is read for the last time is {y} ")
print(f"The number of different words until we hear the first word for the last time is {z}")
