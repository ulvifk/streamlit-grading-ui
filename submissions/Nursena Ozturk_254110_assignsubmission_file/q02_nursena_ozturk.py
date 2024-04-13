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
for i in range(k,n+1):
    sum = 0
    s = 1
    counter = 0
    while sum<=i:
        sum += 1/s
        s += 1
        counter += 1    
    my_dict.setdefault(i,counter)

print(my_dict)

