############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

number_1 = int(input("Enter choice 1: "))
nlist = []


while (0> number_1) or (number_1> 9) :
    print("Please choose a numeral from 0 to 9.")
    number_1 = int(input("Enter choice 1: "))
nlist.append(number_1)    
  

  
number_2 = int(input("Enter choice 2: "))
while number_2 in nlist:
    print("Please choose a different numearal at each time.")
    number_2 = int(input("Enter choice 2: "))
while (0> number_2) or (number_2> 9) :
    print("Please choose a numeral from 0 to 9.")
    number_2 = int(input("Enter choice 2: "))
nlist.append(number_2)    


number_3 = int(input("Enter a choice 3:"))
while number_3 in nlist:
    print("Please choose a different numeral at each time. ")
    number_3 = int(input("Enter choice 3: "))
while (0 > number_3) or (number_3 > 9):
    print("Please choose a numeral from 0 to 9.")
    number_3 = int(input("Enter choice 3: "))
nlist.append(number_3)

number_4 = int(input("Enter a choice 4:"))
while number_4 in nlist:
    print("Please choose a different numeral at each time. ")
    number_4 = int(input("Enter choice 4: "))
while (0 > number_4) or (number_4 > 9):
    print("Please choose a numeral from 0 to 9.")
    number_4 = int(input("Enter choice 4: "))
nlist.append(number_4)


print(nlist)