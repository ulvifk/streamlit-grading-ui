k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
results = {}

for k in range(3, 21):
    sum_terms = 0
    n = 1
    while sum_terms < k:
        sum_terms += 1 / n
        n += 1
    results[k] = n - 1

print(results)