############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choiceList = []

while len(choiceList) < 4:
    choice = input(f"Enter choice {len(choiceList) + 1}: ")
    choice = int(choice)
    if choice < 0 or choice > 9:
        print("Please choose a numeral from 0 to 9.")
    elif choice in choiceList:
        print("Please choose a different numeral at each time.")
    else:
        choiceList.append(choice)


print("Your choices are:", choiceList)