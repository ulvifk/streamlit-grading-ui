lottery_list=[]
while len(lottery_list)<4:
    my_choice=int(input('Please enter number: '))
    if (my_choice)<0:
        print('please choose a numeral from 0 to 9.')
    elif my_choice>9:
        print('please choose a numeral from 0 to 9.')
    else:
        if my_choice not in lottery_list:    
            lottery_list.append(my_choice)
        else:
            print('Please choose a different numeral at each time.')

print(lottery_list)
