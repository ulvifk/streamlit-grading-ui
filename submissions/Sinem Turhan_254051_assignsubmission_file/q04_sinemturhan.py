############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []
while len(choices) < 4:
    choice = input(f"Enter choice {len(choices) + 1}: ")
    if not choice.isdigit():
        print("Please choose a numeral from 0 to 9.")
        continue
    choice = int(choice)
    if choice < 0 or choice > 9:
        print("Please choose a numeral from 0 to 9.")
        continue
    if choice in choices:
        print("Please choose a different numeral at each time.")
        continue
    choices.append(choice)

print(f"Your choices are {choices}.")
