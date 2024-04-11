choices, i = [], 1
while len(choices) < 4:
    choice = int(input(f"Enter choice {i}: "))
    if choice not in range(10):
        print("Please choose a numeral from 0 to 9.")
    elif choice in choices:
        print("Please choose a different numeral at each time.")
    else:
        choices.append(choice)
        i += 1
print(f"Your choices are {choices}.")