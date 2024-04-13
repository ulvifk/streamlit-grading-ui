k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

liste = [i for i in range (k,n+1)]
dic = dict.fromkeys(liste)

for i in dic.keys():
    sum = 1
    z = 2
    while sum < i:
        sum += 1/z
        z += 1
    dic[i] = z-1
    
print(dic)
