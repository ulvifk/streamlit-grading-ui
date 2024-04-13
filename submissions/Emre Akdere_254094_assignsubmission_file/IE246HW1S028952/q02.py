k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

result= {}

for k in range(3,21):
    summ = 0
    n =1
    while summ < k:
        summ += 1/n
        n += 1
    result[k] = n
    

        