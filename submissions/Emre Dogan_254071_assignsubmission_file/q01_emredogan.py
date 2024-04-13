my_string = " in the end it is not the years in your life that count it is the life in your years "

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

a = list(my_string.split(" "))
a.pop()
a.remove("")

count = 0
for i in range(len(a)):
    count += 1
    if a[-1] == a[i]:
        break
 

b = a[::-1]
cou = 0
for i in range(len(a)):
    cou += 1
    if a[0] == b[i]:
        cou -= 1
        break
   
ad = set()
for i in range(len(a)):
    ad.add(a[i])
    if a[0] == a[i] and a[0] not in a[i::]:
        break
      

shortsizedstring = f"The number of words to be read until the last word of the test is heard for the first time is {count}."
shortsizedstring += f"The number of remaining words after the first word is read for the last time is {cou}. The number"
shortsizedstring +=f"of different words until we hear the first word for the last time is {len(ad)}."    
print(shortsizedstring)