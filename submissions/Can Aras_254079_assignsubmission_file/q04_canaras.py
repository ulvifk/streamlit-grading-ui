############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choice_list = []
i = 1

choice = int(input(f"Enter choice {i}:"))
while i < 5:
    if choice in choice_list:
        print("You must enter different numerals")
        choice = int(input(f"Enter choice {i}: "))
    elif choice > 9 or choice < 0:
        print( "Please choose a numeral from 0 to 9.")
        choice = int(input( f"Enter choice {i}: "))
    else :
        choice_list.append(choice)
        i += 1
        if i < 5:
            choice = int(input(f"Enter choice {i}:"))
    
    
print(f"Your choices are {choice_list}")
