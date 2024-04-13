############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

my_choices = []

while len(my_choices) < 4:
    my_choice = input("Choose your number from 0 to 9: ")

    if my_choice.isdigit():
        num = int(my_choice)
        if 0 <= num <= 9 and num not in my_choices:
            my_choices.append(num)
        elif num in my_choices:
            print("Choose another number.")
        else:
            print("Number should be from 0 to 9.")
    else:
        print("Enter a valid number.")

print("My choices are:", my_choices)







