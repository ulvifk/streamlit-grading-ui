k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

for i in range(k,n+1):
    j = 1
    summ = 0
   
    while summ <= i:
        num = 1/j
        summ += num
        j+=1
   
    harmonic_dic = {} # empty dictionary
    harmonic_dic[i]=j-1
    
    print(harmonic_dic)