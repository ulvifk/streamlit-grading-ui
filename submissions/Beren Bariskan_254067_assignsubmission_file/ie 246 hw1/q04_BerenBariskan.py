############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
mylist=list()
t=0
while t<4:
    x=int(input("Please enter a number from 0 to 9, both inclusive: "))
    if x<0 or x>9:
        print("Please enter a number in the given interval: ")
    elif x in mylist:
        print("Please enter a different number: ")
    else:
        mylist.append(x)
        t+=1
print(mylist)