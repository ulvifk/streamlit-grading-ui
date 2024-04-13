my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list = list(my_string.split(" "))
rev_liste = my_list[:]
rev_liste.reverse()
m = my_list.index(my_list[-1])
k = rev_liste.index(my_list[0])
y = k
new_list = []
for i in rev_liste[k:]:
    if i not in new_list:
        new_list.append(i)
z = len(new_list)




print(f"The number of words to be read until the last word of the text is heard for the first time is {m}")
print(f"The number of remaining words after the first word is read for the last time is {y} ")
print(f"The number of different words until we hear the first word for the last time is {z}")