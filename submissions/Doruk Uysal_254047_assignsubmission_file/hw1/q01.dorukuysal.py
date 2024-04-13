my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################
my_string = "in the the years in your life that count it is the life in your years"
my_str_sep = my_string.split(" ")

last = my_str_sep[-1]
first= my_str_sep[0]
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
for i in my_str_sep:
    if i != last:
        counter_1 += 1
    else:
        counter_1 += 1
        break


for j in my_str_sep[::-1]:
    if j != first:
        counter_2 += 1
    else:
        break


for k in my_str_sep[::-1]:
    if k != first:
        counter_3 += 1
    else:
        counter_3 += 1
        break
diff = my_str_sep[:-counter_3]

set_hali = set(diff)

        
print(f"The number of words to be read until the last word of the test is heard for the first time is {counter_1} .")
print(f"The number of remaining words after the first word is read for the last time is {counter_2} .")
print(f"The number of different words until we hear the first word for the last time is {len(set_hali)} .")
