my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

w = list(my_string.split(" "))


number_1 = 0
for i in range(len(w)):
    number_1 += 1
    if w[-1] == w[i]:
        break
    
w_r = w[::-1]
number_2 = 0
for i in range(len(w)):
    number_2 += 1
    if w[0] == w_r[i]:
        number_2 -= 1
        break
    
ad = set()
for i in range(len(w)):
    ad.add(w[i]) 
    if w[0] == w[i] and w[0] not in w[i::]:
        break
    
short_sized_string = f"""The number of words to  be read until the last word of the test is heard  for the first time is {number_1}. """

short_sized_string += f"""The number of remaining words after the first word is read for the last time is {number_2}. """

short_sized_string += f"""The number of different words until we hear the first word for the last time is {len(ad)}. """
print(short_sized_string)