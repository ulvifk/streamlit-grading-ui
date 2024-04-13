k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


dictof_reqnum = {}
listof_reqnum = []
a=k

#creates list of required numbers

while(a<n+1):
    listof_reqnum.append(a)
    a=a+1
    
#defines each key of the list a "None" value

for a in listof_reqnum:
    dictof_reqnum[a] = None

firstnum=1
i=k
b=1

# updates the dict with the new harmonic series values which is found by iterating
# each time a new number is added and equals the required value to the new one

while (i<n+1):
    if firstnum==1:
        c=b
    else:
        b=c+(1/firstnum)
    if b<i:
        firstnum=firstnum+1 
        c=b
    else: 
        dictof_reqnum[i] = firstnum    
        i=i+1
print(dictof_reqnum)





