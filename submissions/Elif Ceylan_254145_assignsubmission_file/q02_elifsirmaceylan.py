# Question 2 - Elif Sırma Ceylan

keys=[]
values=[]

my_dict={}

for k in range(3,21):
    n=1
    result=0
    while result<k:
        result+=(1/n)
        n+=1
        keys.append(k)
        values.append(n-1)

my_dict = dict(zip(keys, values))

print(my_dict)
        
