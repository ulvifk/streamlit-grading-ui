k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
sum=0
times=0
divider=0
mydict=dict()
for i in range(k,n+1):
    while sum<i:
        divider+=1
        sum=sum+1/divider
        times+=1
        mydict[i]=times
print(mydict)
        
    
            