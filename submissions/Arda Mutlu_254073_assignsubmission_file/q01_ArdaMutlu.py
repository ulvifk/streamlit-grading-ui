# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:35:31 2024

@author: Lenovo
"""
my_string= "in the end it is not the years in your life that count it is the life in your years"
mylist=my_string.split(" ")
lastword=mylist[-1]
firstword=mylist[0]   #Bu soruya index yoluyla farklı çözümler de olabilirdi fakat loopla uzun da olsa içime sindi
calculator2=0
firstwordcount=0
emptylist=[]
calculator3=0
firstwordcount2=0
print(f"The number of words to be read until the last word of the test is heard for the first time is {mylist.index(lastword)+1}.")
for j in mylist:
    if j==firstword:
        firstwordcount+=1
        calculator2+=1
        if firstwordcount==3:
            print(f"The number of remaining words after the first word is read for the last time is {len(mylist)-calculator2}.")
            break
    else:
        calculator2+=1
for k in mylist:
    if k==firstword:
        emptylist.append(k)
        firstwordcount2+=1
        calculator3+=1
    else:
        calculator3+=1
        emptylist.append(k)
myset=set(emptylist)
wordcount=len(myset)
print( f"The number of different words until we hear the first word for the last time is {wordcount}.")