k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

def my_sum(k):
    n = 1
    total = 0
    while total < k:
        total += 1 / n
        n += 1
    return n

result_dict = {}
for k in range(3, 21):
    result_dict[k] = my_sum(k)

print(result_dict)