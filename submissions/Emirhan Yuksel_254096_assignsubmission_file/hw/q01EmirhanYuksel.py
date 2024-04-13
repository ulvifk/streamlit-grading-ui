my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
my_list=list(my_string.split(" "))
x=my_list.index(my_list[-1])

reverse_my_list=my_list[:]
reverse_my_list.reverse()

m = reverse_my_list.index(my_list[0])

y = m

t = []
for i in reverse_my_list[m:]:
    if i not in t:
        t.append(i)
        
z = len(t)

print(f"The number of words to be read until the last word of the text is heard for the first time is {x+1}")
print(f"The number of remaining words after the first word is read for the last time is {y} ")
print(f"The number of different words until we hear the first word for the last time is {z}")



