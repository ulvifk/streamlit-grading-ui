############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
lottery_numbers = []
while len(lottery_numbers) < 4:
    number = int(input("Enter a lottery numeral (0-9): "))   
    if 0 <= number <= 9:
        lottery_numbers.append(number)
    else:
        print("Please choose a numeral from 0 to 9.")
print("Your lottery numbers are:", lottery_numbers)

    