from src.sstgame import wyr
from src.sstgame import numberGuess
from src.sstgame import madlib
from src.sstgame import randomGame



def exampleMadLib():
    print(madlib.madlib())
print("This is the example for the madlib function")
exampleMadLib()

def exampleRandomNumber():
    print(numberGuess.numberGuess())
print("This is the example for the numberGuess function")
exampleRandomNumber()

def exampleWYR():
    print(wyr.wouldYouRather())
print("This is the example for the wouldYouRather function")
exampleWYR()

def exampleRandomGame():
    print(randomGame.randomGame())
print("This is the example for the randomGame function")
exampleRandomGame()