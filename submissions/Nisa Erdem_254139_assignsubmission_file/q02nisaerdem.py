k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def min_terms_for_sum(k):
    n = 1
    current_sum = 0
    while current_sum < k:
        current_sum += 1 / n
        n += 1
    return n - 1

result_dict = {}
for k in range(3, 21):
    result_dict[k] = min_terms_for_sum(k)

print(result_dict)
