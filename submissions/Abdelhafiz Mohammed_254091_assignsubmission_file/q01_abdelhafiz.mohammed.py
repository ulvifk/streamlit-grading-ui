#HW 1

#QUESION 1

def calculate_word_counts(text):
    words = text.split()
    word_count = len(words)
    unique_words = set(words)

    first_word_last_occurrence_index = len(words) - 1 - words[::-1].index(words[0])
    words_until_last_word_first_occurrence = first_word_last_occurrence_index + 1
    remaining_words_after_last_word_first_occurrence = word_count - first_word_last_occurrence_index - 1
    different_words_until_last_word_first_occurrence = len(set(words[:first_word_last_occurrence_index + 1]))

    return (words_until_last_word_first_occurrence,
            remaining_words_after_last_word_first_occurrence,
            different_words_until_last_word_first_occurrence)

my_string = "in the end it is not the years in your life that count it is the life in your years"

results = calculate_word_counts(my_string)
print(f"The number of words to be read until the last word of the text is heard for the first time is {results[0]}.")
print(f"The number of remaining words after the first word is read for the last time is {results[1]}.")
print(f"The number of different words until we hear the first word for the last time is {results[2]}.")
