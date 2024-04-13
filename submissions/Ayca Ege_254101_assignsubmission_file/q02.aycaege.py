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

for i in range(k, n+1):
    j = 1
    sum_terms = 0
    while sum_terms < i:
        sum_terms += 1 / j
        j += 1
    my_dict[i] = j - 1
print(my_dict)