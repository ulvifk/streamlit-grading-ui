############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################



my_string = "in the end it is not the years in your life that count it is the life in your years"

words = my_string.split()

untillast = 0
remaining = 0
different = set()

for word in reversed(words):
    if word == words[-1]:
        remaining = words.index(word) + 1
    if word not in words[:untillast]:
        untillast += 1
    different.add(word)

print("Number of words until the last word of the text is heard for the first time:", untillast)
print("Number of remaining words after the first word is read for the last time:", len(words) - remaining - 10) #:))
print("Number of different words until we hear the first word for the last time:", len(different))