############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices = []
k=0
while(k<4):
    a = int(input(f"Enter your guess: "))
    if a<0:
        print("Please enter a positive number.")
    elif a>9:
        print("Please enter a number between 0 and 9.")
    elif a in choices:
        print("Please enter a different number.")
    else:
        choices.append(a)
        k+=1

print(f"Your choices are {choices}.")






