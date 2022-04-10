from operator import truediv
import random



def getInput():
    print('inside input function')
    return input('enter a guess: ')


def randomNumber():
    print('inside random number')
    return random.randrange(1,10)

# == equals
# != doesn't equal
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

# Strings 'words hello, hi'
# Integers 5 4 8 100
# Boolean True False

continueGame = True
guessCorrect = 0

while continueGame == True:
    randomlyGeneratedNumber = random.randrange(1,10)
    userGuess = input('Enter a guess: ')
    if userGuess == 'e':
        continueGame = False
        continue

     # IF statement starts here
    if randomlyGeneratedNumber == int(userGuess):
        print('hooray')
        guessCorrect = guessCorrect + 1 
        print(guessCorrect) 
    else:
        print('boo you suck, the correct value was ' + str(randomlyGeneratedNumber))
    
    print('To end game, enter e')

# this prints the variable guessCorrect
print(guessCorrect)
# this prints the word "guessCorrect"
print('guessCorrect')
# this creates a variable and sets the value of whatever the guessCorrect variable is at the time


       
 



# THIS IS JUST FOR YOUR REFERENCE. GREEN TEXT DOESN'T GET RUN BY THE COMPUTER
# i = 1
# while i < 6:
#     print(i)
#     i = i + 1
# print('í is greater than six now, have a good day.!!!!!fjaiofwehjfouiwehfuiow')



   