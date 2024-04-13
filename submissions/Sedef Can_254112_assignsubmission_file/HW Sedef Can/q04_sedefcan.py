############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

list_choice = []
a = 0

while a < 4:
    list_choice_2 = int(input(f"Enter choice {a+1}: "))
    if list_choice_2 < 0 or list_choice_2 > 9:
        print("Please choose a numeral from 0 to 9.")
    elif list_choice_2 in list_choice:
        print("Please choose a different numeral at each time.")
    else: 
        list_choice.append(list_choice_2)
        a += 1
        
print(f"Your choices are {list_choice}")