my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string_split = my_string.split(" ")

for i in range(len(my_string_split)):
    stop = my_string_split.index(my_string_split[-1])
    word = stop + 1

print(f"The number of words to be read until the last word of the text is heard for the first time is {word}. ")

for i in range(len(my_string_split)):
    stop_point = my_string_split[::-1].index(my_string_split[0])
    count = abs(stop_point)
    
print(f"The number of remaining words after the first word is read for the last time is {count}.")

my_string = "in the end it is not the years in your life that count it is the life in your years"
my_string_split = my_string.split()

sum = 0
seen_words = set()

for word in my_string_split:
    if word not in seen_words:
        seen_words.add(word)
        sum += 1

print(f"The number of different words until we hear the first word for the last time is {sum}.")


