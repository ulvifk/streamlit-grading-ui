############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

# Initialize an empty list to store user choices
choices = []

# Function to check if a choice is valid
def is_valid_choice(choice):
    return isinstance(choice, int) and 0 <= choice <= 9 and choice not in choices

# Function to prompt user for input and validate it
def get_valid_choice(number):
    while True:
        choice = input("Enter choice {}: ".format(number))
        try:
            choice = int(choice)
            if is_valid_choice(choice):
                return choice
            else:
                print("Please choose a numeral from 0 to 9 and make sure it's not submitted already.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Prompt user for choices
for i in range(1, 5):
    choice = get_valid_choice(i)
    choices.append(choice)

# Print the final choices
print("Your choices are {}.".format(choices))