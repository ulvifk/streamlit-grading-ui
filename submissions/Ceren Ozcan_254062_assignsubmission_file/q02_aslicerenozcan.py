k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict ={}

for j in range(k, n+1):
    series_sum = 0
    term_index = 1
    num_terms = 0
    
    while series_sum < j:
        series_sum += 1 /term_index
        term_index+= 1
        num_terms += 1
    my_dict[j] = num_terms


print(my_dict)


    