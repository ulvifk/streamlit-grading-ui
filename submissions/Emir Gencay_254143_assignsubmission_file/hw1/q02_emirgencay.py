dictionary = {}  

for num in range(3, 19): #it lasts too long if i wrote there range(2,21) due to try it i wrote 6. 
    n = 1
    wholesum = 0
    
    while wholesum < num:
        wholesum += 1 / n
        n += 1
    
    dictionary[num] = n - 1
    
print(dictionary)

## An alternative way
"""dictionary = {}

n = 1
wholesum = 0
k= input("Write number from 3 to 20: \n")

while wholesum <int(k):
    wholesum+= 1/n
    n+=1

print(n-1)"""