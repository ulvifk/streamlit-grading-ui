############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################
emty_list=[]
x=0
while x<=3:
    cevap=int(input("0 t0 9 a kadar bir sayı giriniz. ikiside dahil."))
    if (cevap<0 or cevap>9):
        print("Please choose a numeral from 0 to 9.")
    else:
        if (cevap not in emty_list):
            emty_list.append(cevap)
            x+=1
print(emty_list)    
