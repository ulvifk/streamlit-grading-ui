############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

choiceslist = []
a = 0
while a < 4 :
    choices_inlist = int(input(f"Enter choice {a + 1}: "))
    if choices_inlist < 0 or choices_inlist > 9 :
        print("Please choose a numeral from 0 to 9.")
    elif choices_inlist in choiceslist :
        print("Please choose a different numeral at each time.")
    else:
        choiceslist.append(choices_inlist)
        a += 1
print(f"Your choices are {choiceslist}.") 
         
        