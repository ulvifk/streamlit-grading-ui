############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices, i = [], 1
while i<=4:
    choice = int(input(f"Enter Choice {i}:"))
    if choice not in range(10):
        print("Please choose a numeral from 0 to 9.")
    elif choice in choices:
        print("Please choose a different numeral at each time.")
    else:
        choices.append(choice)
        i+=1

print(f"Your choices are {choices}.")
