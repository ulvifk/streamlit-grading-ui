my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words_in_string = my_string.split()    #to split the given string to it's words for using them later

first_word_of_string = words_in_string[0]   #with this operation I reached the first word
positions_of_words = [0]                   #to storing each word's position in given string
at_the_moment = 0                          # variable to storing current position

for word in words_in_string:
    if word == first_word_of_string:
        positions_of_words.append(at_the_moment)
    at_the_moment += 1
    
num_of_last_first_word = positions_of_words[-1] + 1   #number of the words to be read until the last word of the
                                                      #text is heard for the first time
                                                      
after_last_first = words_in_string[positions_of_words[-1] + 1: ] #with this line spyder split words list into two parts
                                                                 # last occurence of first word (before / after)
                                                                 
remaining = len(after_last_first)                     #number of remaining words which are after the first word is read for the last time

diff_words = len(set(words_in_string[:positions_of_words[-1]]))  #to find number of different words
                                                                 #until we notice first word for the last time
                                                                 
print(f"The number of words to be read until the last word of the text is heard for the first time is "
      f"{num_of_last_first_word}.\n "
      f"The number of remaining words after the first word is read for the last time is {remaining}.\n"
      f"The number of different words until we hear the first word for the last time is {diff_words}.\n")