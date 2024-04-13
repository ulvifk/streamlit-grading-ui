############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
your_choices = []
def four_numbers():
    choices = []

    for i in range(1, 5):
        while True:
            try:
                number = int(input(f"Enter choice {i}: "))
                if 0 <= number <= 9 and number not in your_choices:
                    your_choices.append(number)
                    break
                elif number in your_choices:
                    print('Please choose a different numeral at each time.')
                else:
                    print('Please choose a number between 0 and 9.')
                    
            except ValueError:
                print('Invalid input. Please enter an integer.')

    print("Your choices are", your_choices)

four_numbers()
