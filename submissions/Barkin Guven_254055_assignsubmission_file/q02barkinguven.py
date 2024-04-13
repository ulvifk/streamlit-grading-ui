k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dict={}
for i in range(3,19):
    n=1
    tumtoplam=0
    
    while tumtoplam<i:
        tumtoplam += 1 / n
        n += 1
    
    dict[i] = n - 1
    
print(dict)