k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
mydict=dict()
sum=0
divisor=0
trials=0
for i in range (k,n+1):
    while sum<i:
        divisor+=1
        sum=sum+(1/divisor)
        trials+=1
        mydict[i]=trials
print(mydict)
