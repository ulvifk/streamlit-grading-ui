k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

result_dict = {}

for k in range(3, 21):
    current_sum = 0
    terms = 0
    while current_sum < k:
        terms += 1
        current_sum += 1 / terms
    result_dict[k] = terms

print("Dictionary of minimal number of terms needed in the finite harmonic series:")
print(result_dict)
