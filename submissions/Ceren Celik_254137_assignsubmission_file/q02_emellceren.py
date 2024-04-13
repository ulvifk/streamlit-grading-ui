k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

harmonic_sums = {}
for x in range(k, n+1):
    y = 1
    while True:
        if sum(1/i for i in range(1, y+1)) >= x:
            harmonic_sums[x] = y
            break
        y += 1


print(harmonic_sums)