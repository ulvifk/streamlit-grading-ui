############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

#range 10
#int input " Enter choice "
# if number < 0

count = 1
number_list = []

while count < 5:
    
    number = int(input(f"Enter choice {count}: "))
    
    if (number<0):
        print("Please choose a numeral from 0 to 9.")
        
    elif (number > 9):
        print("Please choose a numeral from 0 to 9.")
    
    
    elif (number in number_list):
        print("Please choose a different numeral at each time.")
        
    else:
        number_list.append(number)
        count+=1
        
print(f"Your choices are {number_list}.")
    