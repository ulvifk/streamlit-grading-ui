# Question 1 - Elif Sırma Ceylan

my_string = "in the end it is not the years in your life that count it is the life in your years"

list_of_words = my_string.split()

num_words_until_last_occurrence = list_of_words.index(list_of_words[-1]) + 1

print(f"The number of words to be read until the last word of the test is heard for the first time is {num_words_until_last_occurrence}.", end=" ")


count_of_words = {}

for word in list_of_words:
    if word in count_of_words:
        count_of_words[word] += 1
    else:
        count_of_words[word] = 1

first_word = list_of_words[0]
last_index = 0


for i, word in enumerate(list_of_words):
    if word == first_word:
        last_index = i

remaining_words = len(list_of_words) - last_index - 1

print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.", end=" ")


unique_word_set = set()
first_word = list_of_words[0]
last_index = len(list_of_words) - 1

for J in range(len(list_of_words) - 1, -1, -1):

    if list_of_words[J] == first_word:
        last_index = J
        break

for i in range(last_index):
    unique_word_set.add(list_of_words[i])

num_different_words = len(unique_word_set)

print(f"The number of different words until we hear the first word for the last time is {num_different_words}.")
