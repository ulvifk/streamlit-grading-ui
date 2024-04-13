

my_string = "in the end it is not the years in your life that count it is the life in your years"


words=list()
words=my_string.split()
lastword=words[-1]
criticindex=words.index(lastword)
question1=criticindex+1


firstword=words[0]
wordsreversed=words[::-1]
question2=wordsreversed.index(firstword)


countword=len(words)
a=words[0:countword-wordsreversed.index(firstword)]
question3 = len(set(a))

print(f"""The number of words to be read until the last word of the test is heard for the first time is {question1}.
The number of remaining words after the first word is read for the last time is {question2}. 
The number of different words until we hear the first word for the last time is {question3}.""")

