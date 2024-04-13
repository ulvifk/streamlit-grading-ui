k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

# Initialize an empty dictionary to store the results
result_dict = {}

# Iterate over integers from 3 to 20
for k in range(3, 21):
    # Initialize variables to keep track of the sum and number of terms
    sum_terms = 0
    num_terms = 0
    
    # Add terms to the sum until it is greater than or equal to k
    while sum_terms < k:
        num_terms += 1
        sum_terms += 1 / num_terms
    
    # Store the minimal number of terms needed in the dictionary
    result_dict[k] = num_terms

# Print the dictionary
print(result_dict)
