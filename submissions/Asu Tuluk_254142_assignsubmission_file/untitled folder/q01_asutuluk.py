my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_string = "in the end it is not the years in your life that count it is the life in your years"
list=my_string.split(" ")
count=0
for i in list:
    last=list[len(list)-1]
    if (i==last):
        count+=1
        break
    else:
        count=count+1
print(f"The number of words to be read until the last word of the text is heard for the first time is {count}.")



my_string = "in the end it is not the years in your life that count it is the life in your years"
list=my_string.split(" ")
count=0
for k in range(len(list)):
    if (list[0]==list[::-1][k]):
        break
print(f"The number of remaining words after the first word is read for the last time is {k}.")


my_string = "in the end it is not the years in your life that count it is the life in your years"
list=my_string.split(" ")
count=0
for k in range(len(list)):
    if (list[0]==list[::-1][k]):
        break
    list=list[:k:-1]
new=(set(list))
print(f"The number of different words until we hear the first word for the last time is {len(new)}.")

