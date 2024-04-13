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
    summation = 0
    limit = 1
    while summation < i:
        summation += 1/limit
        limit += 1
    my_dict[i] = limit - 1
print(my_dict)