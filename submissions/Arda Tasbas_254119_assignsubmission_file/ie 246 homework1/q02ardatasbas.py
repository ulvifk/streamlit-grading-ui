mydict = {}

for i in range(3,21):
    harmonum = 0
    count = 1
    while(harmonum <= i):
        harmonum += 1/count
        count += 1
    mydict[i] = (count-1)
    
print(mydict)


        