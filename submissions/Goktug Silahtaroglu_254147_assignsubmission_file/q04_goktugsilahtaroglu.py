############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
n=0
mylist=[]
while n<4:
    a=int(input("Enter a number between 0-9: "))
    if a<0 or a>9:
        print("Please enter a correct number: ")
    elif a in mylist:
        print("enter a different number: ")
    else:
        mylist.append(a)
        n+=1
print(mylist)

