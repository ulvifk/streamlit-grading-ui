############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
print("Please enter four numerals from 0 to 9.")
choices_list=[]

while len(choices_list)<1:
    first_input=int(input("enter first choice: "))
    if first_input<0 or first_input>9: 
        print("please choose a numeral from 0 to 9.")
    elif first_input in choices_list:
        print("please choose a numeral from 0 to 9.")
    else:
        choices_list.append(first_input)
        
        while len(choices_list)<2:
            second_input=int(input("enter second choice: "))
            if second_input<0 or second_input>9:
                print("please choose a numeral from 0 to 9.")
            elif second_input in choices_list:
                print("please choose a numeral from 0 to 9.")
            else:
                choices_list.append(second_input)
                
                while len(choices_list)<3:
                    third_input=int(input("enter third choice: "))
                    if third_input<0 or third_input>9:
                        print("please choose a numeral from 0 to 9.")
                    elif third_input in choices_list:
                        print("please choose a numeral from 0 to 9.")
                    else:
                        choices_list.append(third_input)
                        
                        while len(choices_list)<4:
                            fourth_input=int(input("enter fourth choice: "))
                            if fourth_input<0 or fourth_input>9:
                                print("please choose a numeral from 0 to 9.")
                            elif fourth_input in choices_list:
                                print("please choose a numeral from 0 to 9.")
                            else:
                                choices_list.append(fourth_input)
print(f"your choices are {choices_list}")
            


