k = 3
n = 21

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
dict = {}

    
tries = 0
i = 1
sum = 0

for a in range(k,n):
    while sum < a:
        sum = sum + 1/i
        tries = tries + 1
        i = i + 1
        if sum >= a:
            dict[a] = tries
            
print(dict)
