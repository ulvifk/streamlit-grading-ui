k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

myDict={}

for i in range(k,n+1):
    iterationcount = 0
    harmonic = 1
    total = 0
    while total < i:
        total = (1/harmonic)
        iterationcount += 1
        harmonic += 1
    myDict[i] = iterationcount
print(myDict)
