############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

kupon = []
count = 0
while count < 4:
    try:
        number = int(input("Please enter a numeral between 0 and 9 (inclusive): "))
        if 0 <= number <= 9 and number not in kupon:
            kupon.append(number)
            print("Numeral " + str(number) + " chosen.")
            count += 1
        else:
            print("Invalid. Choose different.")
    except ValueError:
            print("Invalid. Choose integer.")
            
print("Your choices are: ", kupon)