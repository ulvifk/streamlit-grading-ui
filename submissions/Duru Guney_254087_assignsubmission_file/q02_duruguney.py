k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

harmonic_sum={}
number=1
current_sum=0
for num in range(3,21):
    while current_sum<num:
        current_sum+=1/number
        number+=1
        harmonic_sum[num]=number-1
         
print(harmonic_sum)
        