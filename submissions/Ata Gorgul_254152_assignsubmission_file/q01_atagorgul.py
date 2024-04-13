my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


my_string = "in the end it is not the years in your life that count it is the life in your years"

string_list = my_string.split()
print(string_list)
a = string_list[-1]

b = string_list[:string_list.index(a)+1]
print(len(b))


sub_string = string_list[-1::-1]

c = string_list[0]
d = sub_string[:sub_string.index(c)]

print(len(d))
different_words = set(sub_string[sub_string.index(c) + 1:])
      
        
print(len(different_words))

