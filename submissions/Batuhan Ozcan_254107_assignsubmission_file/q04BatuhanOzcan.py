############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

my_choices = []

while len(my_choices) < 4:
    choice = int(input(f"Enter choice {len(my_choices) + 1}: "))
    
    if choice < 0 or choice > 9:
        print("Please choose a numeral from 0 to 9.")
    elif choice in my_choices:
        print("Please choose a different numeral at each time.")
    else:
        my_choices.append(choice)

print("Your choices are")
print(my_choices)