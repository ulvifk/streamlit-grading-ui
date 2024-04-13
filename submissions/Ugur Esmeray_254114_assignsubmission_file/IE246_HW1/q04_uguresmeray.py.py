############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
# Initialize an empty list to store the user's choices
user_choices = []

while len(user_choices) < 4:
    # Ask for user input
    user_input = input(f"Enter choice {len(user_choices) + 1}: ")
    
    try:
        # Attempt to convert the input to an integer
        num = int(user_input)
        
        # Check if the number is within the allowed range and not already chosen
        if 0 <= num <= 9:
            if num not in user_choices:
                # If valid and unique, add it to the list
                user_choices.append(num)
            else:
                # If the number has already been chosen, inform the user
                print("Please choose a different numeral at each time.")
        else:
            # If the number is outside the allowed range, inform the user
            print("Please choose a numeral from 0 to 9.")
    except ValueError:
        # If the input is not an integer, inform the user (though the prompt assumes integer input)
        print("Invalid input. Please enter an integer.")

# Once four unique numbers are chosen, display the list to the user
print(f"Your choices are {user_choices}.")

