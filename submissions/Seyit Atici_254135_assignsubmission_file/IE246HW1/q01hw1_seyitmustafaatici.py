my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list = my_string.split(" ")
last_word = my_list[-1]

counter1 = 0
for word in my_list:
    counter1 += 1
    if word == last_word:
        break
print("Index of the last word:", counter1)

# Finding the index of the first word in the given sentence (reversed)
reverse_list = my_list[::-1]
first_word = my_list[0]
counter2 = 0
for word in reverse_list:
    if word == first_word:
        break
    counter2 += 1
print("Index of the first word (reversed):", counter2)

# Removing duplicate words
unique_words = []
for word in my_list[::-1]:
    if word not in unique_words:
        unique_words.append(word)
counter3 = len(unique_words)
print("Length of the sentence after removing duplicates:", counter3)

print(f"The number of words to be read until the last word of the test is heard for the first time is {counter1}. The number of remaining words after the first word is read for the last time is {counter2}. The number of different words until we hear the first word for the last time is {counter3}.")