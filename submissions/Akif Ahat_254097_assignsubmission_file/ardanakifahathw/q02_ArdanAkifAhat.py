k = 3
n = 21

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

# WAIT FOR A WHILE FOR IT TO WORK


mydict = dict()
for i in range(k,n):
    sum = 1.0
    t = 1.0
    while sum < i:
        t += 1
        sum += (1.0/t)
    mydict[i] = t
    
print(mydict)
    