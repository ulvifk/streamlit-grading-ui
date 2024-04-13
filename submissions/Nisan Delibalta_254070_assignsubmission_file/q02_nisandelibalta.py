k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

result = {}

for k in range(3,21):
    finite_sum = 0
    n = 1
    while finite_sum <= k:
        finite_sum += 1/n
        n += 1
    result[k] = n-1
    
print(result)