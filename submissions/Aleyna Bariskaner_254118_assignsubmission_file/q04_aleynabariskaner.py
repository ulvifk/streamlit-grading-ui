############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################





numbers = []
while len(numbers) < 4:
    inp = int(input("Enter choice " + str(len(numbers)+1) + ":"))
    if inp in numbers:
        print("Please choose a different numeral at each time.")
    elif inp < 0 or inp > 10:
        print("Please choose a numeral from 0 to 9.")
    else:
        numbers.append(inp)
print("Your choices are " + str(numbers) + ".")

