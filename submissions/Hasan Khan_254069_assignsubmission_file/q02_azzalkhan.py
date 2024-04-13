k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dict1 = {}
for k in range(3, 21):
    n = 1
    sum1 = 0

    while sum1 < k:
        sum1 += 1 / n
        n += 1

    dict1[k] = n - 1

print(dict1)
