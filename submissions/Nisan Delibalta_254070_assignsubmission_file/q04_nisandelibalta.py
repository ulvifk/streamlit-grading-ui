############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []

while len(choices) < 4 :
    choice = int(input(f"Enter choice {len(choices)+1}: ")) 
    
    if choice < 0 or choice > 9:
        print(f"Please choose a numeral from 0 to 9")
    elif choice not in choices:
        choices.append(choice)
    else:
        print("Please choose a different numeral at each time.")
        
print(f"Your choices are {choices}")
        
        
        
        
    
    
    