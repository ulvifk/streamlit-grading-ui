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
        a = int(input(f"Enter choice {i}: "))
        if a >= 0 and a <= 9 :
            if a not in choices:
                choices.append(a)
                break
            else: 
                print("Please choose a different numeral at each time. ")
        else: 
            print("Please choose a numeral from 0 to 9. ")

print(f"Your choices are {choices}.")