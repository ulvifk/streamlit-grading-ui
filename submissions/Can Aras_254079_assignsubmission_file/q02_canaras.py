k = 3
n = 21

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

mydict = {}

    
iterations = 0
i = 1
summation = 0

for b in range(k,n):
    while summation < b:
        summation += 1/i
        iterations += 1
        i = i + 1
        if summation >= b:
            mydict[b] = iterations
            
print(mydict)
