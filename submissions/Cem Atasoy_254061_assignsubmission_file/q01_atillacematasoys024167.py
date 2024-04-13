"""
soru1
"""

my_string = "in the end it is not the years in your life that count it is the life in your years"

words = my_string.split()

lasta_word = words.index(words[-1]) + 1

print(f"Number of words to be read until the last word of the text is heard for first {lasta_word}.")


ix_firstword = len(words) - words[::-1].index(words[0]) - 1

lasta_word = words[:ix_firstword + 1]

wordsleft = (len(words)- len(lasta_word))

print(f"Number of remaining words after first word is read for last time is {wordsleft}.")


ix_firstword = len(words) - words[::-1].index(words[0]) - 1

lasta_word = words[:ix_firstword + 1]

differ_lasta_word = len(set(lasta_word))


print(f"Number of different words until we hear first word for last time is {differ_lasta_word}.")