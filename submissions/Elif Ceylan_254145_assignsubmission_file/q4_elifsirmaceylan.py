# Question 4 - Elif Sırma Ceylan

choices, i = [], 1

while i<=4:

    choice = int(input(f"Enter Choice {i}:"))
	
    if choice not in range(10):
        print("Please choose a numeral from 0 to 9.")
		
    elif choice in choices:
        print("Please choose a different numeral at each time.")
		
    else:
        choices.append(choice)
        i+=1

print(f"Your choices are {choices}.")