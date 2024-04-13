############################################################################
# Write your script down below.
# Your script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choices=[]
i=len(choices)
while i < 4:
    choice=input("enter choice "+ str(i+1)+ ":")

    if 0<=int(choice)<=9:
        if choice not in choices:
            choices.append(choice)
            i += 1
        else:
            print("Please choose a different numeral each time.")
    else:
        print("Please choose a numeral from 0 to 9.")

print(f"Your choices are {choices}")
