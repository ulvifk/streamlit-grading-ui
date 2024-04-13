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
k = 3
while k <= n:
    hsum = 0 
    adder = 1
    counter = 0
    while hsum < k :
        hsum += 1 / adder
        counter += 1
        adder +=1
    my_dict[k] = counter
    k += 1
    
print(my_dict)