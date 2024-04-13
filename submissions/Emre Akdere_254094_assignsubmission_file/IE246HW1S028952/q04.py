############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

pool = [0,1,2,3,4,5,6,7,8,9]
choices=[]

while len(choices)<4:
    i = int(input(f"Enter choice {len(choices)+1}:"))
    if i in pool:
        choices.append(i)
        pool.remove(i)
    elif i in choices:
        print("Select different one than previous")
    else:
        print("Please select a numeral between 0 to 9")
if len(choices)==4:
    print(f"Your choices are {choices}")

        
        
    
    
       