k = 2
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
sözlük = {}
summ = 0
count = 0
i = 1
while True:
    summ += 1/i
    i +=1
    count +=1
    if summ >= k:
        sözlük[k]=count
        k += 1
        if n+1 == k:
            break
print(sözlük)    