############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choice = []
while len(choice) <4:
    num = int(input(f"Enter choice {len(choice) + 1} "))
    if 0<= num and num>=9:
        if num not in choice:
            choice.append(num)
        else:
            print("Please choose a different number at each time")
    else:
        print("Please choose a number from 0 to 9")

print(f"Your choices are {choice}")
