my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
def analyze_text(my_string):
    words = my_string.split()  # Split the string into a list of words
    first_word = words[0]  # The first word
    last_word = words[-1]  # The last word

    # The number of words to be read until the last word of the text is heard for the first time
    last_word_first_appearance = words.index(last_word) + 1

    # The number of remaining words after the first word is read for the last time
    first_word_last_appearance = len(words) - 1 - words[::-1].index(first_word)
    remaining_words = len(words) - first_word_last_appearance - 1

    # The number of different words until we hear the first word for the last time
    unique_words_until_first_word_last = len(set(words[:first_word_last_appearance + 1]))

    return last_word_first_appearance, remaining_words, unique_words_until_first_word_last

my_string = "in the end it is not the years in your life that count it is the life in your years"
last_word_first_appearance, remaining_words, unique_words_until_first_word_last = analyze_text(my_string)

print(f"The number of words to be read until the last word of the test is heard for the first time is {last_word_first_appearance}.")
print(f"The number of remaining words after the first word is read for the last time is {remaining_words}.")
print(f"The number of different words until we hear the first word for the last time is {unique_words_until_first_word_last}.")
