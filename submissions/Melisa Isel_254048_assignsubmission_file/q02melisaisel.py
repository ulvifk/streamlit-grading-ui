k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

sum_terms = 0
num_terms = 0

while sum_terms < k :
    num_terms += 1
    sum_terms += 1 / num_terms
    
    result_dict = {}
    for k in range(k,n+1):
        result_dict[k] = num_terms
        
print(result_dict)
