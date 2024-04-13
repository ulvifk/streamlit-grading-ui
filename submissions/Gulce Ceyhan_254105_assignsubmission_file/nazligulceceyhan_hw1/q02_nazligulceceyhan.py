k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

solution = {}   #a dictionary to store expected results

for key in range(3,21):  #this range can be changed according to k and n values
    terms = 1            #terms(variable) for storing number of terms
    sum_of_values = 1    #sum of the first term in harmonic series
    
    while sum_of_values < key:
        terms += 1 
        sum_of_values = sum(1 / x for x in range(1,terms+1) )
    solution[key] = terms

print(solution)    
        