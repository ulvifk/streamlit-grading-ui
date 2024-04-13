my_string = "in the end it is not the years in your life that count it is the life in your years"

############################################################################
# You may change the string, but don't change the variable name 'my_string'
# Above code will be used in testing your script.
# Write your script down below.
# Be cautious about the syntax and logic.
############################################################################

kelimeler=list()
kelimeler=my_string.split()
son_kelime=kelimeler[-1]
criticindex=kelimeler.index(son_kelime)
Qone=criticindex+1


ilk_kelime=kelimeler[0]
wordsreversed=kelimeler[::-1]
Qtwo=wordsreversed.index(ilk_kelime)


countword=len(kelimeler)
a=kelimeler[0:countword-wordsreversed.index(ilk_kelime)]
Qthree = len(set(a))

print(f"""The last word of the test is heard for the first time is {Qone}.
The number of remaining words after the first word is read for the last time is {Qtwo}. 
The number of different words until we hear the first word for the last time is {Qthree}.""")
liste=[]
for i in range(18):
    if kelimeler[i] not in liste:
        liste.append(kelimeler[i])

print(liste)