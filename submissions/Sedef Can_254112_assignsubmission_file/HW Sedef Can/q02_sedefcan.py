k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dict_x = {}
list_x = []
a = k

while (a < n + 1):
    list_x.append(a)
    a = a + 1
    
for a in list_x:
    dict_x[a] = None

first_num = 1   
i = k 
b = 1 

while (i < n + 1):
    if first_num == 1:
        c = b
    else:
        b = c + (1/first_num)
    if b<i:
        first_num = first_num + 1
        c = b
    else: 
        dict_x[i] = first_num
        i = i + 1
        
print(dict_x)

        
