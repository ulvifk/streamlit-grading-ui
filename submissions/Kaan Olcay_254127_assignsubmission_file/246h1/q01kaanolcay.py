

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"
wor= my_string.split(" ")

lastw = wor[-1]
a=wor.index(lastw)+1
print(f"number of words to be read until the last word of the test is heard for the first time is {a}.")

firstw = wor[0]
wordsre = wor.copy()
wordsre.reverse()
b=wordsre.index(firstw)
print(f"number of remaining words after the first word is read for the last time is {b}.")

firstwlastindex = len(wor) - wordsre.index(firstw) - 1
words_last_index = wor[:firstwlastindex]
c=len(set(words_last_index ))
print(f"The number of different words until we hear the first word for the last time is {c}.")

