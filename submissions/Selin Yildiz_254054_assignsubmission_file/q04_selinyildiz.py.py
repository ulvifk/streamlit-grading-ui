############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choice_list =[]

while len(choice_list) < 4:
    choice = int(input(f"Enter choice {len(choice_list) + 1 }."))
   
    if choice < 0 or choice > 9:
        print("Please enter a numeral from 0 to 9.")
        
    elif choice in choice_list:
        print("Please choose a different numeral at each time.")
        
    else:
        choice_list.append(choice)
        
print(f"Your choices are {choice_list}.")

    