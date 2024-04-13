my_string = "in the end it is not the years in your life that count it is the life in your years"
words = my_string.split(" ")

#a
last_word = words[-1]
print(f"The number of words to be read until the last word of the test is heard for the first time is {words.index(last_word)+1}.")

#b
first_word = words[0]
words_reverse = words.copy()
words_reverse.reverse()
print(f"The number of remaining words after the first word is read for the last time is {words_reverse.index(first_word)}.")

#c
first_word_last_index = len(words) - words_reverse.index(first_word) - 1
words_until_first_word_last_index = words[:first_word_last_index]
print(f"The number of different words until we hear the first word for the last time is {len(set(words_until_first_word_last_index))}.")


