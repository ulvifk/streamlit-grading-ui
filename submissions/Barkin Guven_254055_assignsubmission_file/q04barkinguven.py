############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of "range"
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
########################################################################


all_choices=[]
print('Pls enter 4 numbers betwwen 0-9 include both')
while len(all_choices) <4:
    try:
        number= int(input(f"Enter choice {len(all_choices) + 1}: "))
        if 0 <= number <= 9:
           if number not in all_choices:
              all_choices.append(number)
           else:
               print("Please dont write the same number.")
        else:
            print("Please choose a number between 0 and 9.")
    except:
         print("Please provide an integer.")

print(f"Your choices are: {all_choices}")
    