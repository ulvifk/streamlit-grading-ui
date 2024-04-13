############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

def get_valid_input(choices):
    while True:
        choice = input(f"Enter choice {len(choices) + 1}: ")
        try:
            choice = int(choice)
            if choice < 0 or choice > 9:
                print("Please choose a numeral from 0 to 9.")
            elif choice in choices:
                print("Please choose a different numeral at each time.")
            else:
                choices.append(choice)
                return choices
        except ValueError:
            print("Please enter a valid integer.")


def main():
    choices = []
    while len(choices) < 4:
        choices = get_valid_input(choices)

    print(f"Your choices are {choices}")


if __name__ == "__main__":
    main()
