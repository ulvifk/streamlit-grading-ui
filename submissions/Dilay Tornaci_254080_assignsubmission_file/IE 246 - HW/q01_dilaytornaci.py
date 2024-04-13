my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

## PART A ###

my_string = my_string.split( )
number = []
for i in my_string:
    if i == my_string[-1]:
        number.append(i)
        break
    else:
        number.append(i)

print(f"The number of words to be read until the last word of the test is heard for the first time is {len(number)}")

# ## PART B ###

# my_string = my_string.split( )
# number = []
# my_string_reverse = my_string[::-1]

# a = my_string_reverse.index(my_string[0])

# for i in my_string[0:-a]:
#     number.append(i)

# print(number)
# print(f"The number of remaining words after the first word is read for the last time is {len(my_string)-len(number)}.")
    
    

# ## PART C ###  

# my_string = my_string.split( )
# number = []
# my_string_reverse = my_string[::-1]
# a = my_string_reverse.index(my_string[0])
# a=a+1

# for i in my_string[0:-a]:
#     if i not in number:
#         number.append(i)
        
# print(f"The number of different words until we hear the first word for the last time is {len(number)}")
        

    
    
    
    
    
    
    


    