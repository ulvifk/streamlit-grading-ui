
my_string = "in the end it is not the years in your life that count it is the life in your years"

list = my_string.split(" ")

lastword = list[-1]
indices1 = []

for i in range(len(list)):
    if list[i] == lastword:
        indices1.append(i)
indices1=[]
for i in range(len(list)):
        if list[i] == list[-1]:
            indices1.append(i)
out1 = str(indices1[0]+1)
firstword = list[0]
indices2 = []

counter = 0
for i in range(len(list)):
    counter += 1
    if list[i] == firstword:
        counter = 0

out2 = counter

distinct = []
for i in range(indices1[-1]-1):
    if list[i] not in distinct:
        distinct.append(list[i])
out3 = len(distinct)

print(
" The number of words to be read until the last word of the test is heard for the first time is "+str(out1)+
". The number of remaining words after the first word is read for the last time is "+str(out2)+". The number"
"of different words until we hear the first word for the last time is "+str(out3)+"."
)
