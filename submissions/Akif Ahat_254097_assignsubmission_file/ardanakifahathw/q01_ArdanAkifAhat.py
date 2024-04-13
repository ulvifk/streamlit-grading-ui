my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

y = my_string.split()

last_word = y[-1]
first_question = []

for i in y:
    first_question.append(i)
    if i == last_word:
        break

first_question_count = len(first_question)

first_word = y[0]
z = reversed(y)
second_question = []

for j in z:
    second_question.append(j)
    if j == first_word:
        break

second_question_count = len(second_question)
last_question_list = y[0:len(y)-second_question_count]

last_question = []

for k in y:
    if k not in last_question:
        last_question.append(k)
        

last_question_count = len(last_question)    
    
    
        
print("The number of words to be read until the last word of the test is heard for the first time is", first_question_count)
print("The number of remaining words after the first word is read for the last time is", second_question_count - 1)
print("The number of different words until we hear the first word for the last time is", last_question_count)