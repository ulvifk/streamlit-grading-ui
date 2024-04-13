k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

dictionary = dict()

for i in range(k,n + 1):
    terms = 1
    summation = 0
    
    while (True):
        summation = summation + (1 / terms)
        terms = 1 + terms
        
        if(summation >= i):
            break
        
        
    dictionary.setdefault(i,terms - 1)
    
text = 'Final dictionary where the values are minimal number of terms needed to be added'
text += ' up in the finite harmonic series to get a sum that is greater than or '
text += 'equal to these keys:\n'

print(text,dictionary)