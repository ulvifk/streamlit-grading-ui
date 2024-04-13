############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################


choices = []
i=1

while i<5:
    x = int(input(f"Enter choice {i}: "))
    if x<0 or x>9:
        print("Please choose a numeral from 0 to 9.")
    elif x in choices:
        print("Please choose a different numeral at each time.")
    else:
        choices.append(x)
        i+=1
print(f"Your choices are: {choices}")
    
        
    