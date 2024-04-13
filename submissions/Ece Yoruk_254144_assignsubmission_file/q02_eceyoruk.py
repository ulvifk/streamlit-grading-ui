k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict={}

for k in range(3,21):
    sum_of_num=0
    num_of_terms=0
    
    while sum_of_num<k:
        num_of_terms+=1
        sum_of_num+=1/num_of_terms
    
        my_dict[k]= num_of_terms

print(my_dict)