k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict = {}
for k in range(3, 21):
    n = 1
    sum_of_terms = 0
    while sum_of_terms < k:
        sum_of_terms += 1 / n
        n += 1
    my_dict[k] = n - 1

print(my_dict)