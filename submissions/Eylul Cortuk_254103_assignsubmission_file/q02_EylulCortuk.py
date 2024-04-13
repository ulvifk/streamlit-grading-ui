k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dictionary={}
for i in range(k,n+1):
    x=1
    y=0
    while y < i:
        y = y + 1/x
        x = x+1
    dictionary[i]=x-1
    
print(dictionary[5])

