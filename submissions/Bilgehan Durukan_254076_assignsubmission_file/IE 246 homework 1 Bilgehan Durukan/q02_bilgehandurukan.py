


harmonic_dict = {}

for k in range(3, 21):
    harmonic_sum = 0
    n = 1
    while harmonic_sum < k:
        harmonic_sum += 1 / n
        n += 1
    harmonic_dict[k] = n - 1

print(harmonic_dict)

    
    
    


