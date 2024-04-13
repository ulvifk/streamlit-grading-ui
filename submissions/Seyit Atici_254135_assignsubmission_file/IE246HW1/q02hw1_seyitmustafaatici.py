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

for i in range(k,n+1): # n+1 'e kadar range alıyorum çünkün'de dahil olsun.
    totalsum = 0
    c = 1
    counter = 0
    while totalsum <= i:
        totalsum += 1/c
        c += 1
        counter += 1    
    my_dict.setdefault(i,counter)

print(my_dict)

# Kod çalışıyor fakat n=20 olduğunda çok fazla loop olduğundan çok uzun sürüyor
# Sayıları küçültüp denemenizi tavsiye ederim
