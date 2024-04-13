my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

#the number of words to be read until the last word of the text is heard for the first time:
def sentence_length(x):
    num_of_words=x.split()
    
seen_words=()
for i in range(len(num_of_words)):
      word=num_of_words[i]
      seen_words.append(i)
if word in seen_words:
        word