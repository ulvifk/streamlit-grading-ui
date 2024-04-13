############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

answers = []

def choice():
        x = int(input(f"Enter choice {i+1}: "))
        if x > 9:
            print("Please choose a numeral from 0 to 9.\n")
            choice()
        elif x < 0:
            print("Please choose a numeral from 0 to 9.\n")
            choice()
        elif x in answers:
            print("Please choose a different numeral at each time.\n")
            choice() 
        else:
            answers.append(x)

for i in range(4):
    choice()
   
print("Your choices are", answers)