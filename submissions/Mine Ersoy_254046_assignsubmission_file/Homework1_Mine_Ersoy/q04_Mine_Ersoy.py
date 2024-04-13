############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
my_list = []
k = 1
while k < 5:
    try:
        m = int(input(f"Enter choice {k}: "))
        if m in my_list:
            print("Please choose a different numeral at each time")
        elif m >= 0 and m < 10:
            my_list.append(m)
            k += 1
        else:
            raise ValueError
    except ValueError:
        print("Please choose a numeral from 0 to 9")
print(my_list)