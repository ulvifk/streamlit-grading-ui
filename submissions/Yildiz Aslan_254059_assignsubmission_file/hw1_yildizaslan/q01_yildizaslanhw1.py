my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

last_word = my_string.split(" ")[-1]
first_word = my_string.split(" ")[0]

concat_str = ""
counter = 0

for txt in my_string.split(first_word)[:len(my_string.split(first_word)) - 1]:
    concat_str += txt
    if(txt == ""):
        counter += 1
        
concat_str = concat_str.strip()

word_list = []
for word in concat_str.split():
    if(word not in word_list):
        word_list.append(word)
dif_word_counter = len(word_list) + counter

print("The number of words to be read until the last word of the text ('",last_word,"') is heard for the first time :",
      len(my_string.split(last_word)[0].split()) + 1)

print("The number of remaining words after the first word ('",first_word,"') is heard for the last time :",
      len(my_string.split(first_word)[-1].split()))

print("the number of different words until we hear the first word ('",first_word,"') for the last time :",
      dif_word_counter)        