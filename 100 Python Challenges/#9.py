#Question 9
#Level 2

'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''

sentencelist = []

while True: 
    sentence = input("Please enter sentence. Or enter 'done', when you are finished: ")
    if sentence == 'done':
        break
    else:
        sentencelist.append(sentence)
        
for i in sentencelist:
    print(i.upper())
