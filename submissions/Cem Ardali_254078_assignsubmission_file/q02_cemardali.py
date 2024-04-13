k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

harmonic_dict = {}

for k in range(3,21):
    n = 1
    sum_terms = 0
    
    while sum_terms < k:
        sum_terms += 1 / n
        n += 1
        
    harmonic_dict[k] = n - 1

print("Dictionary of minimal number of terms needed for the finite harmonic series:")
for key, value in harmonic_dict.items():
    print(f"For k = {key} , minimum terms needed: {value}")
    
    