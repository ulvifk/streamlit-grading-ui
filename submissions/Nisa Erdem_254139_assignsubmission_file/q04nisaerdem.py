############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

def get_lottery_choices():
    choices = []
    while len(choices) < 4:
        choice = input("Enter choice {}: ".format(len(choices) + 1))
        try:
            choice = int(choice)
            if choice < 0 or choice > 9:
                print("Please choose a numeral from 0 to 9.")
            elif choice in choices:
                print("Please choose a different numeral at each time.")
            else:
                choices.append(choice)
        except ValueError:
            print("Please enter a valid integer.")

    return choices

# Get the lottery choices from the user
lottery_choices = get_lottery_choices()

# Print the final choices
print("Your choices are", lottery_choices)
