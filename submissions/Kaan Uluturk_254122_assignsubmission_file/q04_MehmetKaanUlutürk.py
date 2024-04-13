############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

def get_lottery_game():
    lottery_numbers = []

    for i in range(1, 5):
        while True:
            try:
                num = int(input(f"Enter choice {i}: "))
                if num < 0 or num > 9:
                    print("Invalid input! Please enter a numeral between 0 and 9.")
                elif num in lottery_numbers:
                    print("You've already entered this numeral. Please enter a different one.")
                else:
                    lottery_numbers.append(num)
                    break  
            except ValueError:
                print("Invalid input! Please enter a numeral between 0 and 9.")
    print("Your choices are:", lottery_numbers)
    return lottery_numbers

lottery_numbers = get_lottery_game()