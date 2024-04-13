############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
#########################################################################

choices = []
print("Welcome to the lottery game.")
print("Please choose 4 different numerals from 0 to 9.")

while len(choices) < 4:
    choice = input("Enter choice: ")
    try:
        num = int(choice)
        if num < 0 or num > 9:
            print("Please choose a numeral from 0 to 9.")
        elif num in choices:
            print("Please choose a different numeral.")
        else:
            choices.append(num)
    except ValueError:
        print("Please enter a numeral.")

print(f"Your choices are {choices}.")
