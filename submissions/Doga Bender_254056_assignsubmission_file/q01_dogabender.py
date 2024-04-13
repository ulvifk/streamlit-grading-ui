my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

a = list(my_string.split())

for i in range(len(a)):
    if a[i] == a[-1]:
        words_read = i+1
        break
        
for j in range(len(a),0,-1):
    if a[j-1] == a[0]:
        remaining_words = len(a)-j
        break
    
new_list = []
for k in range(len(a)-remaining_words+1):
    new_list.append(a[k])
    answer = set(new_list)
    different_words = len(answer)
    

print(f"The number of words to be read until the last word of the test is heard for the first time is {words_read}."
      f"The number of remaining words after the first word is read for the last time is {remaining_words}." 
      f"The number of different words until we hear the first word for the last time is {different_words}.")

