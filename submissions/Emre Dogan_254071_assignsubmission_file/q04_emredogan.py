############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
i = 1
liste = []
while len(liste)<4:
    a = int(input(f" Enter choice {i} "))
    if a in liste:
            print("Please choose a different numeral at each time.")
    elif a<= 9 and a>0:
        i+= 1
        liste.append(a)
    elif a<0 or a>9:
        print("Please choose a numeral from 0 to 9.")
print(f"Your choices are {liste}")        