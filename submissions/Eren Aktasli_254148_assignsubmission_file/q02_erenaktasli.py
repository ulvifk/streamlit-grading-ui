k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def find_min_terms(k_range):
    result_dict = {}

    for k in k_range:
        sum_terms = 0
        n = 0

        while sum_terms < k:
            n += 1
            sum_terms += 1/n
            
        result_dict[k] = n

    return result_dict

k_range = range(3, 21)
result = find_min_terms(k_range)
print(result)