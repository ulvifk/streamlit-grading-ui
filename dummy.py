############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

x_1 = int(input("Enter choice 1: "))
alist = []


while (0> x_1) or (x_1> 9) :
    print("Please choose a numeral from 0 to 9.")
    x_1 = int(input("Enter choice 1: "))
alist.append(x_1)    
  

  
x_2 = int(input("Enter choice 2: "))
while x_2 in alist:
    print("Please choose a different numearal at each time.")
    x_2 = int(input("Enter choice 2: "))
while (0> x_2) or (x_2> 9) :
    print("Please choose a numeral from 0 to 9.")
    x_2 = int(input("Enter choice 2: "))
alist.append(x_2)    


x_3 = int(input("Enter a choice 3:"))
while x_3 in alist:
    print("Please choose a different numeral at each time. ")
    x_3 = int(input("Enter choice 3: "))
while (0 > x_3) or (x_3 > 9):
    print("Please choose a numeral from 0 to 9.")
    x_3 = int(input("Enter choice 3: "))
alist.append(x_3)

x_4 = int(input("Enter a choice 4:"))
while x_4 in alist:
    print("Please choose a different numeral at each time. ")
    x_4 = int(input("Enter choice 4: "))
while (0 > x_4) or (x_4 > 9):
    print("Please choose a numeral from 0 to 9.")
    x_4 = int(input("Enter choice 4: "))
alist.append(x_4)


print(alist)