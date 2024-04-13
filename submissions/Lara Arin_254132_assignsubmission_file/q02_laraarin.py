k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


empty_dict = {}
sum_of_numbers = 0
n=1

for i in range(2,21):
    while sum_of_numbers <= i:
        sum_of_numbers += 1/n
        n+=1
        empty_dict[i] = n-1
print(empty_dict)
        