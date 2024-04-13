""" 
soru 2
"""

k = 3
n = 20


harmonicpedia = {}

for k in range(3,21):
    n = 1
    sumofterms = 0
    
    while sumofterms < k:
        sumofterms += 1 / n
        n += 1
        
    harmonicpedia[k] = n - 1

print("Dict of minimal number of terms needed for finite harmonic series:")
for key, value in harmonicpedia.items():
    print(f"For k = {key} , minimum terms needed: {value}")