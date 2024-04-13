k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

mydict = {}

for k in range(3,21):
    harmonu = 0
    coun = 1
    while(harmonu <= k):
        harmonu += 1/coun
        coun += 1
    mydict[k] = (coun-1)
    
print(mydict)



    