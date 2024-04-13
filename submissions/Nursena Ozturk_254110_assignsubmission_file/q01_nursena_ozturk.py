my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_list = my_string.split(" ")
last_word = my_list[-1] 

a = 0  #kaç kez for döngüsü dönüyor diye sayıyor.
for i in my_list:
    a += 1
    if i == last_word:
        break
print(a)


reverse_list = my_list[::-1]
first_word = my_list[0]
b = 0
for j in reverse_list:
    
    if j == first_word:
        break
    b +=1 
print(b)
    

reverse_list = my_list[::-1]
first_word = my_list[0]
c=0
for i in reverse_list:
    if i == first_word:
        break
    c += 1
n_list = reverse_list[c:]
finishlist = []
for i in n_list:
    if i not in finishlist:
        finishlist.append(i)
d = len(finishlist)
print(d)       

print(f"The number of words to be read until the last word of the test is heard for the first time is {a}. The number of remaining words after the first word is read for the last time is {b}. The number of different words until we hear the first word for the last time is {d}.")
        
        