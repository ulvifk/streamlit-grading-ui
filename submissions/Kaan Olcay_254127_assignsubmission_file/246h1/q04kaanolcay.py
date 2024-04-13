############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
choicenum = 1
choi = []

while (choicenum <= 4):
    gue = int(input(f"Enter choice {choicenum}: "))
    if (gue<0 or gue>9):
        print("Please choose a numeral from 0 to 9.")
    elif (gue in choi):
        print("Please choose a different numeral at each time.")
    else:
        choicenum += 1
        choi.append(gue)

print(f"Your choices are {choi}")
