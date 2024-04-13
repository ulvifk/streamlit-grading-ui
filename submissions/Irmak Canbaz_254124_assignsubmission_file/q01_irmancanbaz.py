my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_str_sep = my_string.split(" ")

first_word = my_str_sep[0]
last_word = my_str_sep[-1]

word_counter_1 = 0
word_counter_2 = 0
word_counter_3 = 0
word_counter_4 = 0

for i in my_str_sep:
    if i != last_word:
        word_counter_1 += 1
    else:
        word_counter_1 += 1
        break

for j in my_str_sep[::-1]:
    if j != first_word:
        word_counter_2 += 1
    else:
        break

for k in my_str_sep[::-1]:
    if k != first_word:
        word_counter_3 += 1
    else:
        word_counter_3 += 1
        break
diff_search = my_str_sep[:-word_counter_3]

set_hali = set(diff_search)

        
print(f"The number of words to be read until the last word of the test is heard for the first time is {word_counter_1}.")
print(f"The number of remaining words after the first word is read for the last time is {word_counter_2}.")
print(f"The number of different words until we hear the first word for the last time is {len(set_hali)}.")

