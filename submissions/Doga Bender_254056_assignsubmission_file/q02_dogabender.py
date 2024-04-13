k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict = {}

for i in range(k, n + 1):
    counter = 1
    result = 0
    while True:
        result += 1 / counter
        if result >= i:
            my_dict[i] = counter
            break
        counter += 1

print("Dictionary:", my_dict)
