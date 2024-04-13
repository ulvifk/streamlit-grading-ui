############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choicelist = []
for i in range(5):
    while len(choicelist) < i:
        choice = int(input(f"Enter Choice {i}: "))
        if choice >= 9 or choice <= 0 or choice in choicelist:
            print("Please enter an appropriate number")
            choice
        else:
            choicelist.append(choice)
        


print(choicelist)