k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
def min_terms_to_exceed_k(k):
    sum_terms = 0
    num_terms = 0
    while sum_terms < k:
        num_terms += 1
        sum_terms += 1 / num_terms
    return num_terms

min_terms_dict = {}
for k in range(3, 21):
    min_terms_dict[k] = min_terms_to_exceed_k(k)

print(min_terms_dict)