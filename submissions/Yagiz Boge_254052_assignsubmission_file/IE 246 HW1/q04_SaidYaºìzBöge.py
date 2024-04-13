############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

numbers = []
counter = 1
while len(numbers)<4:
    n = int(input(f"Enter Choice {counter}: "))
    if n >9 or n<0:
        print("Please choose a numeral from 0 to 9.")
    elif n in numbers:
        print("PLease choose a different numeral each time.")
    else:
        numbers.append(n)
        counter += 1
print(f"Your choices are {numbers}.")