my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

list = my_string.split(" ")
list1=[]
list2=[]
list3=[]

for i in range(len(list)):
        if list[i] ==  list[-1]:
            list1.append(i)
q1 = list1[0]+1

counter = 0
for i in range(len(list)):
    counter += 1
    if list[i] == list[0]:
        counter = 0
q2 = counter

list3 = []
for i in range(list1[-1]-1):
    if list[i] not in list3:
        list3.append(list[i])
q3 = len(list3)

print( " The number of words to be read until the last word of the test is heard for the first time is "+str(q1)+
". The number of remaining words after the first word is read for the last time is "+str(q2)+". The number"
"of different words until we hear the first word for the last time is "+str(q3)+".")

