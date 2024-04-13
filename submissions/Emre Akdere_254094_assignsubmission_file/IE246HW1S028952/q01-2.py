my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words = my_string.split()
lastword = words[-1]
firstword = words[0]
lastwordheardfirst = words.index(lastword) + 1
rewords= words[::-1]
wordcount= len(words)

remainingafterfirstheardlast = rewords.index(firstword)
newcut= words[:-3]
unique= set(newcut)
differentword= len(unique)





print(f"The number of words to be read until the last word of the test is heard for the first time is  {lastwordheardfirst}") 
print(f"The number of remaining words after the first word is read for the last time is {remainingafterfirstheardlast}")
print(f"The number of different words until we hear the first word for the last time is {differentword}")