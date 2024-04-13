############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

lot_numbers =[]
i=1
while len(lot_numbers)<4:
    try:
        number = int(input((f"Provide number {i} for lottery between 0 and 9:\t")))
        if number>=0 and number<=9:
            if number not in lot_numbers:
                lot_numbers.append(number)
                i+=1
                print(f"You have entered number {number}")
            else:
                print(f"You have entered same number {number} you have entered before, try another number...")
        else:
            print("You should enter a number between 0 and 9...")
    except ValueError:
        print("Strings can not be converted into integers write a number...")
print(f"Your lottery selection is: {lot_numbers}")       