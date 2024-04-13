############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

count = 0
inp = int(input(f"Enter choice {count+1}: "))
number_list = []
while count < 4:
    if (inp <0 or inp >9):
        print ("Please choose a numeral from 0 to 9.")
        inp = int(input(f"Enter choice {count+1}: "))
    elif inp in number_list:
        print ("Please choose a different numeral at each time.")
        inp = int(input(f"Enter choice {count+1}: "))
    else:
        number_list.append(inp)
        count+=1
        if count < 4:
            inp = int(input(f"Enter choice {count+1}: "))
print("Your choices are",number_list)