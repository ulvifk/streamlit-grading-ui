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
    choice = int(input(f"please enter your choice {len(choices)+1}: "))
    try:
        if choice < 0 or choice > 9:
            print(f"please choose a number from 0 to 9")
        elif choice in choices:
            print(f"this number in also in choices, choose another")
        else:
            choices.append(choice)
    except ValueError:
        print("invalid output. Please enter a numeral")
    
print(f"your choices are {choices}")