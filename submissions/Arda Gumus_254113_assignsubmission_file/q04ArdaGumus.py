############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

mylist = []
k=1
while k < 5:
    x = int(input(f"Enter choice {k}:"))
    if x in mylist:
        print("Please choose a different numeral at each time")
    elif x >= 0 and x < 10:
        mylist.append(x)
        k += 1 
    else:
        print("Please choose a numeral from 0 to 9")
print(mylist)