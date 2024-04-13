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

for k in range (k, n + 1):
    n = 0
    harmonic_sum = 0

    while harmonic_sum < k :
        n += 1
        harmonic_sum += 1/n
    harmonic_dict[k] = n

print(harmonic_dict)   
 
              

