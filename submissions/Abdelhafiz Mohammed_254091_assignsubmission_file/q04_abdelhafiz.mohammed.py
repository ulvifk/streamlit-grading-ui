#q04


def get_user_choices():
    choices = []
    submitted_numerals = set()
    while len(choices) < 4:
        choice = input(f"Enter choice {len(choices) + 1}: ")
        try:
            numeral = int(choice)
            if numeral < 0 or numeral > 9:
                print("Please choose a numeral from 0 to 9.")
            elif numeral in submitted_numerals:
                print("Please choose a different numeral at each time.")
            else:
                choices.append(numeral)
                submitted_numerals.add(numeral)
        except ValueError:
            print("Please enter a valid integer.")
    return choices
user_choices = get_user_choices()
print(f"Your choices are {user_choices}.")
