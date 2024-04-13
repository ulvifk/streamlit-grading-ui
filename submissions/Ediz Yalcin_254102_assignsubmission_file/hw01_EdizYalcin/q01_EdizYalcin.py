my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

wordlist = my_string.split()
length = len(wordlist)
lastword = wordlist[-1]
firstqwords = []

for n in wordlist:
    if n != lastword:
        firstqwords.append(n)
    elif n == lastword:
        firstqwords.append(n)
        print(len(firstqwords))
        break

reversestr = reversed(wordlist)
firstword = wordlist[0]
secondqwords = []

for n in reversestr:
    if n != firstword:
        secondqwords.append(n)
    elif n == firstword:
        print(len(secondqwords))
        break

