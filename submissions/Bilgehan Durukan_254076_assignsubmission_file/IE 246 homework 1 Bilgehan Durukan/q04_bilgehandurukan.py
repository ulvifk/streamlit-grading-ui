

choices = []
while len(choices) < 4:
    try:
        # Ask for input
        user_input = int(input(f"Enter choice {len(choices)+1}: "))
        
        # Check if the input is within the desired range and not already chosen
        if 0 <= user_input <= 9:
            if user_input not in choices:
                choices.append(user_input)
            else:
                print("Please choose a different numeral at each time.")
        else:
            print("Please choose a numeral from 0 to 9.")
    except ValueError:
        print("Please enter an integer.")

print(f"Your choices are {choices}.")


