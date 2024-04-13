k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dict_ = {}
for i in range(k, n+1):
    x = 0
    sum_ = 0
    while sum_ < i:
        x += 1
        sum_ += 1 / x
    dict_[i] = x

print(dict_)