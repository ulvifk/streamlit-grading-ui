number_of_choice = 1
choices = []

while (number_of_choice <= 4):
    guess = int(input(f"Enter choice {number_of_choice}: "))
    if (guess<0 or guess>9):
        print("Please choose a numeral from 0 to 9.")
    elif (guess in choices):
        print("Please choose a different numeral at each time.")
    else:
        number_of_choice += 1
        choices.append(guess)

print(f"Your choices are {choices}")
