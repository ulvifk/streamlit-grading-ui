k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

# Minimum number of terms needed to reach certain sums


result = {}

for k_value in range(3, n+1):
    sum_terms = 1
    i = 2
    while sum_terms < k_value:
        sum_terms += 1 / i
        i += 1
    result[k_value] = i - 1

print("Minimum number of terms needed to be added up in the finite harmonic series:")
for key, value in result.items():
    print("For k = {}, minimum number of terms needed is {}".format(key, value))
