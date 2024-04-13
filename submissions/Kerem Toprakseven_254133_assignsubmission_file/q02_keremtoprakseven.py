k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
last={}
for i in range(3,21):
    n=1
    harmonic=1
    while harmonic<i:
        n+=1
        harmonic+=1/i
    last[i]=n
print(last)
        
        