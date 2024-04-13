k = 2
n = 19

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict = {}
my_list = []  
a = k
while a < n + 1 :
    my_list.append(a)
    a += 1
for a in my_list:
    my_dict[a] = None

firstnum = 1
i = k
b = 1
while i < n + 1 :
    if firstnum == 1:
        c = b
    else:
        b = c + (1/firstnum)
    if b < i :
        firstnum += 1
        c = b
    else:
        my_dict[i] = firstnum 
        i += 1

print(my_dict)