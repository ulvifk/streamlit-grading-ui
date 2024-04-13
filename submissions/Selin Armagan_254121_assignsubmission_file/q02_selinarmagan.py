k = 2
n = 19

############################################################################
# You may change the assigned values of k and n, but don't change the variable 
#     names 'k' and 'n'.
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

my_dict={}
my_list=[]
x=k

while(x<n+1):
    my_list.append(x)
    x=x+1
for x in my_list:
    my_dict[x] = None
num=1
i=k 
y=1

while (i<n+1):
    if num==1:
        z=y
    else:
        y=z+(1/num)
    if y<i:
        num+=1
        z=y
    else:
        my_dict[i]= num 
        i+=1
print(my_dict) 
        