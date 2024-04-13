############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

i=0
num_list=[]

while i<4:
    i+=1
    participant_choice_i=int(input(f"Enter choice {i}.\n"))
    
    
       
    if participant_choice_i<0:
        i-=1
        print("Please enter a positive integer.\n")
    elif participant_choice_i>9:
        i-=1
        print("Please choose a numeral from 0 to 9.\n")
    elif participant_choice_i not in num_list:
        num_list.append(participant_choice_i)
    else:
        i-=1
        print(f"Please choose a different numeral at each time.")
        


print(f"Your choice are {num_list}") 