############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

preferences = []

for n in range(4):
    while True:
        pref = int(input(f"Please provide a number for {n+1}:"))
        if 0 <= pref <= 9 and pref not in preferences:            
            preferences.append(pref)
            break
        else:
            if pref < 0  :
                print("Number that you're providing is not a valid numeral. Please consider a positive number.")                 
            elif pref > 9:
                print("Number that you're providing is not a valid numeral.Please consider a number in given interval.")                 
            else:
                print(f"{pref} has already been taken.Please consider another number in given interval.")
                
print(f"Your numbers are {preferences}.")
            
                
                