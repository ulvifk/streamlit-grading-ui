############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []
print("Please enter 4 different numbers from 0 to 9.")
    
while len(choices) < 4:
    number = int(input(f"Enter choice {len(choices) + 1}: "))
    
    if 0 <= number and number <= 9:
        
        if number not in choices:
            choices.append(number)
        
        else:
            print("Please choose a different numeral at each time.")
    
    else:
        print("Please choose a numeral from 0 to 9.")

print(f"Your choices are: {choices}")