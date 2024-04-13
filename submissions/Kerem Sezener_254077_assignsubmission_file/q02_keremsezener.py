output_dict = {}
for k in range(3, 15):
    sum = 0
    n = 1
    while True:
        sum += 1/n
        if sum >= k:
            output_dict[k] = n
            break
        n += 1

print(output_dict)