############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
choice=1
count=0
answerlist=[]
while count<4:
    x=int(input(f"Enter a choice {choice}: "))
    
    if x<0 or x>9:
        print("Please choose a numeral from 0 to 9.")
        print()
    
    elif x in answerlist:
        print("Please choose a different numeral at each time.")
        print()
        
    else:
        choice+=1
        count+=1
        answerlist.append(x)
        print()
        
print(f"Your choices are {answerlist}." )

        
     