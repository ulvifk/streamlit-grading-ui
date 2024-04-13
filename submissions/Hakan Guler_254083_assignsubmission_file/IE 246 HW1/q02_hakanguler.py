k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################


terms = 0
i = 1
result_dict = {}
result = 0
   
for summation in range(k,n+1)  :
    while True:
        if result < summation:
            result += 1/i
            terms +=1
            i +=1
        else:
            result_dict[summation] = terms
            break
    terms = 0
    i = 1
    result = 0
print(result_dict)
    
        
        
        
    
    
    