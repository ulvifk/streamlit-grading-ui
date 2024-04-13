
choices = []
for i in range(4):
    number = int(input(f"Enter choice {i + 1}: "))

    while True:
        if number < 0 or number > 9:
            print("Please choose a numeral from 0 to 9.")
            number = int(input(f"Enter choice {i + 1}: "))
        elif number in choices:
            print("Please choose a different numeral at each time.")
            number = int(input(f"Enter choice {i + 1}: "))  
        else:
            break
    
    choices.append(number)
    
print("Your choices are", choices)