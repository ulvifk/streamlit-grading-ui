############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

i = 1
j = 5
interval = range(0,10)
result_list = []

while i < j:
    ask = int(input(f"Enter choice {i}: "))
    if ask in interval:
        if ask not in result_list:
            result_list.append(ask)
            i +=1
        else:
            print("Please choose a different numeral at each time.")
    else:
        print("Please choose a numeral from 0 to 9.")
print(f"Your choices are {result_list}.")
        
        
    
    

