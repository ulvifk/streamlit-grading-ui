my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

# 1. (25p) Consider a single string object that consists a very long text containing a very large number of words in it, all in lower case letters, and there is no punctuation. The following is an example where we only have 16 words in the text.
#      my_string = "in the end it is not the years in your life that count it is the life in your years"
# Write a Python program that calculates and prints:
# • the number of words to be read until the last word of the text is heard for the first time (8),
# • the number of remaining words after the first word is read for the last time (2),
# • the number of different words until we hear the first word for the last time (11),
 

x = my_string.split(" ")

wordsUntilLast=0
wordsAfterLastFirst=len(x)
myindex=0


for i in x:
    if i==x[-1]:
        wordsUntilLast+=1
        break
    else:
        wordsUntilLast+=1
        

for k in x:
    if k==x[0]:
        myindex+=1
        wordsAfterLastFirst=len(x)-myindex
    else:
        myindex+=1
        


theNumberofDifferent=len(x[:-wordsAfterLastFirst])
newList=x[:-wordsAfterLastFirst]
l=set(newList)

print(f"The number of words to be read until the last word of the text is heard for the first time: {wordsUntilLast} \nThe number of remaining words after the first word is read for the last time: {wordsAfterLastFirst} \nThe number of different words until we hear the first word for the last time: {len(l)}")