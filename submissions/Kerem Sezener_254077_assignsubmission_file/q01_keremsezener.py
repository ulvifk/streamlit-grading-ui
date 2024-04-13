
my_string = "in the end it is not the years in your life that count it is the life in your years"

my_string_splitted = my_string.split()

last_word = my_string_splitted[-1]
first_word = my_string_splitted[0]

i = 0
while True:
    if my_string_splitted[i] == last_word:
        first_last_word_observed = i + 1
        break
    i += 1
  
j = 1
while True:
    if my_string_splitted[-j] == first_word:
        last_first_word_observed = j - 1
        break
    j += 1

my_string = "in the end it is not the years in your life that count it is the life in your years"

k = 1
while True:
    if my_string_splitted[-k] == first_word:
        break
    k += 1

print(k)
word_idx = len(my_string_splitted) - k
words_list = my_string_splitted[:word_idx + 1]

print(first_last_word_observed)  
print(last_first_word_observed)
print(len(frozenset(words_list)))
