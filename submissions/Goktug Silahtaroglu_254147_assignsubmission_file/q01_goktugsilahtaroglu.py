my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

words=list((my_string.split()))
count=0
count2=0
setwords=set(words)
for i in words:
    count+=1
    if i==words[-1]:
        print("The number of words to be read until the last word of the test is heard for the first time is ",count )
        break
for j in words[::-1]:
    count2+=1
    if j==words[0]:
        print("The number of remaining words after the first word is read for the last time is ",count2-1)
        break
for k in words[::-1]:
    if k==words[0]:
        b=set(words[:words.index(k):-1])
        
        print("the number of different words until we hear the first word for the last time is ",len(b))
        
        break
        
        

    
        

        
        
        
    


    
    
