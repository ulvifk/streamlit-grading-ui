k = 3
n = 20

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

result={}
for number in range(3,20):
    sayac=0
    sum=0
    
    for i in range (1,9999999):
        sum=sum+(1/i)
        sayac+=1
        if (sum>=number ):
            result[number]=sayac
            break
        else:
            continue
print(result)
    