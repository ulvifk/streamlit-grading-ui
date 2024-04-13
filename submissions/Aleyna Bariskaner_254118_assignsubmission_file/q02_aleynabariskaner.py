k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

answer= {}

for i in range(k,n+1):
    total=0
    num_of_terms=0
    while total <i:
        total += 1/(num_of_terms +1)
        num_of_terms+= 1
    answer[i] = num_of_terms
    
print(answer)










