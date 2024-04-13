############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################


choices = []
choice_number = 1

while len(choices) < 4:
    try:
        
        choice_input = input(f"Enter choice {choice_number}: ")
        choice = int(choice_input)

        if 0 <= choice <= 9:

            if choice not in choices:
                choices.append(choice)
                choice_number += 1
            else:
                print("Please choose a different numeral at each time.")
        else:
            print("Please choose a numeral from 0 to 9.")
    
    except ValueError:
       
        print("That's not an integer. Please enter an integer.")


print(f"Your choices are {choices}.")
