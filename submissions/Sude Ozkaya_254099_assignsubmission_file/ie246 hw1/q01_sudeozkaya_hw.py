my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words=my_string.split()
counter=0
dif_words= set()
for i in words:
    counter+=1
    if i not in dif_words:
        dif_words.add(i)
    else:
        break
result_a=counter+1

first_word=words[0]
words_seen=[]

words_reversed=list(reversed(words))
for j in words_reversed:
    words_seen.append(j)
    if j==first_word:
        break
  
result_b=len(words_seen)-1


repeated_words=[]

new_list=words[0:len(words)-result_b]
for k in words:
    if k not in repeated_words:
        repeated_words.append(k)
result_c=len(repeated_words)
print(f"The number of words to be read until the last word of the test is heard for the first time is {result_a}.The number of remaining words after the first word is read for the last time is {result_b}. The number of different words untill we hear the first word for the last time is {result_c}.")