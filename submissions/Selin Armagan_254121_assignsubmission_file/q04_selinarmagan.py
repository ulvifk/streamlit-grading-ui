############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

my_list=[]
x=0
while x<4:
    myin_list=int(input(f"Enter choice{x+1}:"))
    if myin_list<0 or myin_list>9:
        print("Please choose a numeral from 0 to 9.")
    elif myin_list in my_list:
        print("Please choose a different numeral each time.")
    else:
        my_list.append(myin_list)
        x+=1
print("Choices selected:",my_list) 
    
