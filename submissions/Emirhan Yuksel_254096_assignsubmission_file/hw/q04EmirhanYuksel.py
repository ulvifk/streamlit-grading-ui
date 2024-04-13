############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
my_list=[]
x=1
while x<5:
    y=int(input(f"Enter choice {x}: "))
    if y in my_list:
        print("Please choose a different numeral at each time. ")
    elif y>=0 and y<10:
        my_list.append(y)
        x+=1
    else:
        print("Please choose a numeral from 0 to 9. ")
print(f"Your choices are {my_list}.")
