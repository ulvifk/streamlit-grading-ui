############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
###########################################################################

choices_list = []
a = 0

while a < 4:
    choicesin_list = int(input(f"Enter choice {a + 1}: "))
    if choicesin_list < 0 or choicesin_list > 9:
        print("Please choose a numeral from 0 to 9.")
    elif choicesin_list in choices_list:
        print("Please choose a different numeral each time.")
    else:
        choices_list.append(choicesin_list)
        a += 1

print("Choices selected:", choices_list)
