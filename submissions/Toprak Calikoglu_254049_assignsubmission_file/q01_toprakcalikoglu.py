my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

list1=[]

x=my_string.split(" ")
for i in x:
    list1.append(i)
    if(i==x[-1]):
        break
y=len(list1)

print("Number of words to be read until the last word is heard for the first time:", y)
    

words=[]
remaning_words=[]
toplam=0
for i in range(len(x)):
    if x[i]==x[0]:
        toplam=i
z=len(x)- (toplam+1)
print(f"The number of remaining words after the first word is read for the last time is {z}.")
    
for i in range(toplam+1):
    if(x[i]not in words):
        words.append(x[i])
h=len(words)       
print(f"The number of different words until we hear the first word for the last time is {h}.")



















