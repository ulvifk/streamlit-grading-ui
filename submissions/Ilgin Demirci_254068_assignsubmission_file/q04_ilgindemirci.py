############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

user_list = []
while len(user_list) != 4:
    choice = int(input(f"Enter your number {len(user_list)+1}:"))
    if choice <0 or choice > 9:
        print("Please enter a numeral from 0 to 9.")
    elif choice in user_list:
        print("Please enter a different number:")
    else:
        user_list.append(choice)
print(user_list)
