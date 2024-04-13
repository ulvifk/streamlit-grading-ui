k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list=[i for i in range (k,n+1)]
my_dict=dict.fromkeys(my_list)

for i in my_dict.keys():
    sum=1
    x=2
    while sum<i:
        sum+=1/x
    my_dict[i]=x-1
 
print(my_dict)    