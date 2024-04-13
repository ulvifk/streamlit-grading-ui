############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []
i = 1

while i <= 4:
    choice = int(input(f"Enter {i} choice: "))
    
    if choice < 0 or choice >= 10:
        print("Please enter a number between 0 and 10")
    elif choice in choices:
        print("You have choosed this number before, enter a different one.")
    else:
        choices.append(choice)
        i += 1

print(f"Choices: {choices}")