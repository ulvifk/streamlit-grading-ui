k = 2
n = 10

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################




empty_dict = {}

for i in range(k,n+1): 
    total=0
    count=1
    while total<i:
        total += 1/count
        count += 1
    
    empty_dict[i]=count

   

print("Sum of harmonic series for each value of k:", empty_dict)


            
    
print(empty_dict)


    