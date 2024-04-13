k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

sözlük = {}
toplam = 0
say = 0
i = 1
while True:
    toplam += 1/i
    i +=1
    say += 1
    if toplam >= k:
        sözlük[k] = say
        k += 1
        if n+1 == k:
            break
print(sözlük)


        
