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
    sum_of_terms = 0
    num_terms = 0
    i = 1
    while sum_of_terms < k:
        num_terms += 1
        sum_of_terms += 1 / i
        i += 1
    result_dict[k] = num_terms

print(result_dict)
