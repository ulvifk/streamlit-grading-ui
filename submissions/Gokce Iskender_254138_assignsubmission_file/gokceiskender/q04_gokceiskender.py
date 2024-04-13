############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

chs = []
while True:
    ch_1 = int(input("Enter choice 1:"))
    if ch_1 < 0 or ch_1 > 9:
        print("Please choose a numeral from 0 to 9.")    
    elif ch_1 in chs:
        print("Please choose a different numeral at each time.")
    else:
        chs.append(ch_1)
        break
  
while True:   
    ch_2 = int(input("Enter choice 2:"))
    if ch_2 < 0 or ch_2 > 9:
        print("Please choose a numeral from 0 to 9.")
    elif ch_2 in chs:
        print("Please choose a different numeral at each time.")
    else:
        chs.append(ch_2)
        break
        
while True:        
    ch_3 = int(input("Enter choice 3:"))
    if ch_3 < 0 or ch_3 > 9:
        print("Please choose a numeral from 0 to 9.")
    elif ch_3 in chs:
        print("Please choose a different numeral at each time.")
    else:
        chs.append(ch_3)
        break
        
while True:        
    ch_4 = int(input("Enter choice 4:"))
    if ch_4 < 0 or ch_4 > 9:
        print("Please choose a numeral from 0 to 9.")
    elif ch_4 in chs:
        print("Please choose a different numeral at each time.")
    else:
        chs.append(ch_4)
        break
    
print(f"Your choices are {chs}")
    
