

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


harmonic_num={}
for k in range(3,21):
    sum=0
    n=1
    while sum < k:
        sum+=1/n
        n+=1
    harmonic_num[k]=n-1
        
print(harmonic_num)