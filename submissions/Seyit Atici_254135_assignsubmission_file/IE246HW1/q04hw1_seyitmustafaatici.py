############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choice_list = []

for i in range(1, 5):
    x = int(input(f"Enter choice {i}: "))
    while x in choice_list or x < 0 or x > 9:
        if x in choice_list:
            print("Please choose a different numeral at each time.")
        else:
            print("Please choose a numeral from 0 to 9.")
        x = int(input(f"Enter choice {i}: "))
    choice_list.append(x)


print(f"Your choices are {choice_list}.")