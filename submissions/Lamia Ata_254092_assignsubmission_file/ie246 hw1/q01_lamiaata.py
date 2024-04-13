my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words=my_string.split()
last_word = words[-1]
result=0

#the number of words to be read until the last word of the text is heard for the first time ()

for word in words:
    result+=1
    if word==last_word:
        break

#the number of remaining words after the first word is read for the last time ()

f_word = words[0]
result1 =0
reversed_words=words[::-1]

for word in reversed_words:
    if word==f_word:
        break
    result1 +=1

#the number of different words until we hear the first word for the last time ()

a = 0
for rword in reversed_words:
    a += 1
    if f_word == rword:
        break
index = len(words) - a
result2 =0
list1 = []
for word in words[0:index]:
    if word not in list1:
        list1.append(word)
        result2 +=1

print(f"The number of words to be read until the last word of the test is heard for the first time is {result}.\nThe number of remaining words after the first word is read for the last time is {result1}.\nThe number of different words until we hear the first word for the last time is {result2}.")    