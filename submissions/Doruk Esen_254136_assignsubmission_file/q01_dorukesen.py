my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

sentence = my_string.split(" ")
last_word = sentence[-1]
first_count = 0
for word in sentence:
    first_count += 1
    if word == last_word:
        break
print (f"The number of words to be read until the last word of the test is heard for the first time is {first_count}.")

first_word = sentence[0]
second_count = 0
for word in sentence [::-1]:
    second_count += 1
    if word == first_word:
        break
print (f"The number of remaining words after the first word is read for the last time is {second_count-1}.")

third_count = 0
is_in = []
for word in sentence[:len(sentence)-second_count]:
    if word in is_in:
        pass
    else:
        is_in.append(word)
        third_count += 1
print (f"The number of different words until we hear the first word for the last time is {third_count}.")