k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

resultDictionary = {}

for k in range(2, 21):
    finite_sum = 0
    n = 0
    while finite_sum < k:
        n += 1
        finite_sum += 1 / n
    resultDictionary[k] = n
    
print("Minimum number of terms needed to exceed k:")
for k, n in resultDictionary.items():
    print(f"k = {k}: {n} terms")
    
resultDictipnary = {}

for k in range(3,21):
    finite_sum=0
    n=0
    while finite_sum <k:
        n +=1
        finite_sum +=1 /n
        resultDictipnary[k]=n
print("minumum number of terms needed to exceed k:")     

    