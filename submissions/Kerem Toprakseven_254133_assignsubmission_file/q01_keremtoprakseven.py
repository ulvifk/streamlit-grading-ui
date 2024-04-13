my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
my_string=my_string.split()
last_word=my_string[-1]
count={}
for i in my_string:
    count[i]=count.get(i,0)+1
before_word=my_string.index(last_word)+1
remaining=len(my_string)-my_string[:-1].index(last_word)
different=len(count)
print(f"the number of words to be read until the last word of the text is heard for the first time is {before_word}.")
print(f"the number of remaining words after the first word is read for the last time is {remaining}.")
print(f"the number of different words until we hear the first word for the last time is {different}.")