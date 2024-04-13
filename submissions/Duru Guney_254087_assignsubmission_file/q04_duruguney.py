############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

end_user=[]
i=1
while True:
    if len(end_user)==4:
        break
    num=int(input(f'enter a number {i}:'))
    if num<0:
        print('you have entered a non-positive integer.')
    elif num>9:
        print('you have entered a number bigger than 9.')
    elif num in end_user:
        print('you have entered an already chosen number')
    else:
        i+=1
        end_user.append(num)
        
print(end_user)