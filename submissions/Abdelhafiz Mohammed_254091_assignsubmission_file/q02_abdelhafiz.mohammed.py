#HW1
#Q02

def min_terms_to_exceed_k(k):
    n = 1
    sum_terms = 0
    while sum_terms < k:
        sum_terms += 1 / n
        n += 1
    return n - 1

result_dict = {}
for k in range(3, 21):
    result_dict[k] = min_terms_to_exceed_k(k)

print("Minimum number of terms needed to exceed each integer k:")
print(result_dict)
