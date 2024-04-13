############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []

for i in range(1, 5):
    while True:
        choice = int(input("Enter choice " + str(i) + ": "))
        
        if choice < 0 or choice > 9:
            print("Please choose a numeral from 0 to 9.")
        elif choice in choices:
            print("Please choose a different numeral at each time.")
        else:
            choices.append(choice)
            break

print("Your choices are", choices)


