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
    choice = int(input(f"enter choice {len(lottery_numbers_selected) +1}:"))
    
    if choice < 0 or choice > 9:
        print(f"please choose a number from 0 to 9")
        
    elif choice in lottery_numbers_selected:
        print(f"please choose a different numeral at each time")
        
    else:
        lottery_numbers_selected.append(choice)
        
print("your choices are")
print(lottert_numbers_selected)

