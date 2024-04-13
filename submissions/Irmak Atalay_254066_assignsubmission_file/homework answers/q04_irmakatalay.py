############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

lottery_numbers_selected = []

while len(lottery_numbers_selected) < 4:
    choice = int(input(f"Enter choice {len(lottery_numbers_selected) + 1}: "))
    
    if choice < 0 or choice > 9:
        print("Please choose a numeral from 0 to 9.")
    elif choice in lottery_numbers_selected:
        print("Please choose a different numeral at each time.")
    else:
        lottery_numbers_selected.append(choice)

print("Your choices are")
print(lottery_numbers_selected)