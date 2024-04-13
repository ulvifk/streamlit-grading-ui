############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []

for i in range(1, 5):
    while True:
        num = int(input(f"Enter choice {i}: "))
        if 0 <= num <= 9 and num not in choices:
            choices.append(num)
            print(f"Enter choice {i+1}: ")
            break
        elif num < 0 or num > 9:
            print("Please choose a numeral from 0 to 9.")
        else:
            print(f"Please choose a different numeral at each time.\nEnter choice {i}: ")

print("Your choices are", choices)