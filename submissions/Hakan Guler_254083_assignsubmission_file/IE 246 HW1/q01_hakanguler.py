my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

count =  1
my_list = my_string.split(" ")
last_word = my_list[-1]
i = 0
while(my_list[i]!= last_word):
    count +=1
    i +=1
print(f"The number of words to be read until the last word of the test is heard for the first time is {count}")
    
first_word = my_list[0]
my_list_reversed = my_list[-1::-1]
count2 =0
j =0
while(my_list_reversed[j]!=first_word):
    count2 +=1
    j+=1
result = count2
print(f"The number of remaining words after the first word is read for the last time is {result}")

empty_list = list()
for k in range(len(my_list)):
    if(my_list[k]== first_word):
        empty_list.append(k)
different_list = [first_word]
for a in range(0,empty_list[-1]):
        if(my_list[a] not in different_list):
            different_list.append(my_list[a])
            
print(f"The number of different words until we hear the first word for the last time is {len(different_list)}")
            
        
    