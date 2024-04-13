k = 3
n = 20



def find_min_terms(k):
    n = 1
    harmonic_sum = 0

    while harmonic_sum < k:
        n += 1
        harmonic_sum += 1 / n

    return n

result_dict = {k: find_min_terms(k) for k in range(3, 21)}

for key, value in result_dict.items():
    print(f"For k = {key}, at least {int(value)} terms are needed.")

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

