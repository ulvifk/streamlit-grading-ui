k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################



results = {}
for k in range(k, n+1):
  partial_sum = 0
  n = 1
  while partial_sum < k:
    partial_sum += 1 / n
    n += 1
  results[k] = n - 1

print(results) 