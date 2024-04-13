k = 3
n = 20     #####the code works but it takes a bit too long to work

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
harmonic_series_dict={}
for n in range(3,21):
    sum=1.0
    nums=1.0
    while sum<n:
        nums+=1
        sum+=1.0/nums
        
    harmonic_series_dict[n]=nums
    
print(harmonic_series_dict)
 