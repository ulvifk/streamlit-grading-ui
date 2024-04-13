k = 2
n = 10

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
    count = 0
    while sum< i:
        count+=1
        sum+=1/count
        sum = round(sum,4)
        
        
    my_dict[i]= count
    
print(my_dict)