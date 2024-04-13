my_string = "in the end it is not the years in your life that count it is the life in your years"
words= my_string.split(" ")

lastword = words[-1]
a=words.index(lastword)+1
print(f"number of words to be read until the last word of the test is heard for the first time is {a}.")

firstword = words[0]
wordsreverse = words.copy()
wordsreverse.reverse()
b=wordsreverse.index(firstword)
print(f"number of remaining words after the first word is read for the last time is {b}.")

first_word_last_index = len(words) - wordsreverse.index(firstword) - 1
words_until_first_word_last_index = words[:first_word_last_index]
c=len(set(words_until_first_word_last_index))
print(f"The number of different words until we hear the first word for the last time is {c}.")


