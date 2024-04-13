############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

k = 3
n = 20
temp_val = 0
my_dict = {}
counter = 1
for i in range(k,n+1):
    while temp_val < i:
        temp_val += (1/counter)
        counter += 1
    my_dict[i] = counter-1
    print(temp_val)
print(my_dict)  

#The calculations take a while so I printed the threshhold values to show that it worked