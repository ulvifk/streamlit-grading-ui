my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list=[]
my_list= my_string.split(" ")
my_set=set()
last_word=my_list[-1]
first_word=my_list[0]
list_len=len(my_list)

x=my_list.index(last_word)+1
print(f"The number of words to be read until the last word of the text is here for the first time: {x}")

y=my_list[::-1].index(first_word)
print(f"The number of remaining words after the first word is read for the last time:{y}")

numof_wordsread=list_len - y
for i in range(numof_wordsread):
    z=my_list[i]
    my_set.add(z)
e=len(my_set)
print(f"The number of different words untill we hear the first word for the last time:{e}") 