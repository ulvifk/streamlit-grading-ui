############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

i = 1
my_list = []
while i < 5:
    choose = int(input(f"Enter choice {i}: \t"))
    if choose in range(0,10) and choose not in my_list:
        my_list.append(choose)
        i += 1
    else:
        if choose not in range(0,10):
            print("Please choose a numeral from 0 to 9.")
        elif choose in my_list:
            print("Please choose a different numeral at each time")
        continue
print(f"Your choices are {my_list}")