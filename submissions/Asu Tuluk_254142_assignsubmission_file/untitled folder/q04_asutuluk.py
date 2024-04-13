############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

a=[]
i=1
while (i<=4):
    x=str(input(f"Enter choice {i}: "))
    x=int(x)
    if x not in range(0,10):
        print("Please choose a numeral from 0 to 9")
    elif (x in a):
        print("Please choose a different numeral at each time")
    else:
        a.append(x)
        i+=1
print(f"Your choices are {a}")