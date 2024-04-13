############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

end_user = []
n = 1
while True:
    if len(end_user) == 4:
        break
    number = int(input(f"Enter your choice{n}: "))
    if number < 0 :
        print("please write number greater than zero")
    elif number > 9 :
        print("write number smaller than 9")
    elif number in end_user:
        print("please don't write same number")
    else:
        n += 1
        end_user.append(number)
print(end_user)

