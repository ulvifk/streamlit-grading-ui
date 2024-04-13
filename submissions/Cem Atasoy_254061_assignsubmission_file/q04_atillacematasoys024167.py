"""
soru4
"""

wish_me_luck = []
lucky_number = 1

while len(wish_me_luck) < 4:
    try:
        
        luckiness = input(f"Enter choice {lucky_number}: ")
        choice = int(luckiness)

        if 0 <= choice <= 9:

            if choice not in wish_me_luck:
                wish_me_luck.append(wish_me_luck)
                lucky_number += 1
            else:
                print("Give a try for different numeral at each time.")
        else:
            print("Give a try. A numeral from 0 to 9.")
    
    except ValueError:
       
        print("That's not an integer. Enter an integer.")


print(f"Your choices are {wish_me_luck}.")