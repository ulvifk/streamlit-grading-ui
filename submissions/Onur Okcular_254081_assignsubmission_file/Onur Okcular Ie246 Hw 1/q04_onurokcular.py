############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = list()
x = 1 

while (len(choices) < 4):
    choice = int(input(f'Enter choice {x}: '))
    if ((choice < 0) or (choice > 9)):
        print("Please choose a numeral from 0 to 9.")
    else:
        if (len(choices) == 0):
            choices.append(choice)
            x = x + 1
        else:
            if (choice in choices):
                print("Please choose a different numeral at each time.")
            else:
                choices.append(choice)
                x += 1

print(f'Your choices are {choices}.')
