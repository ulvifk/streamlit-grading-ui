k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


k_values = range(k, n+1)


results = {}


harmonic_sum = 0.0
n = 0


for k in k_values:

    while harmonic_sum < k:
        n += 1
        harmonic_sum += 1.0 / n
    
    results[k] = n

print(results)

