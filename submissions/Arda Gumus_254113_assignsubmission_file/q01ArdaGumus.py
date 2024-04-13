my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list=list(my_string.split(" "))

a=my_list.index(my_list[-1])

rmy_list=my_list[:]
rmy_list.reverse()
x= rmy_list.index(my_list[0])

b=x

var=[]
for i in rmy_list[x:]:
    if i not in var:
        var.append(i)
        
y=len(var)

print(f"The number of words to be read until the last word of the text is heard for the first time is {a}")
print(f"The number of remaining words after the first word is read for the last time is {b} ")
print(f"The number of different words until we hear the first word for the last time is {y}")