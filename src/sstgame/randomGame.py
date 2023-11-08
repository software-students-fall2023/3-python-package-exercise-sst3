from src.sstgame import numberGuess
from src.sstgame import madlib
from src.sstgame import wyr
from src.sstgame import anagram
from src.sstgame import hangman
import random
import os



def randomGame(
    minValue=None,
    maxValue=None,
    madLibFile=None,
    wyrFile=None,
    numberGuessAssert=True,
    madLibAssert=True,
    wyrAssert=True,
    hangmanFile=None,
    hangmanAssert=True,
    anagramAssert = True
):
    index = 0
    numberGuessIndex = -1
    madLibIndex = -1
    wyrIndex = -1
    anagramIndex = -1
    hangmanIndex = -1

    # Check which games to include.
    if numberGuessAssert == True:
        numberGuessIndex = index
        index += 1

    if madLibAssert == True:
        madLibIndex = index
        index += 1

    if wyrAssert == True:
        wyrIndex = index
        index += 1

    if anagramIndex == True :
        anagramIndex = index
        index +=1
        
    if hangmanAssert == True:
        hangmanIndex = index
        index += 1

    if index == 0:
        print("All games were excluded. No games were chosen!")
        return -1

    # Choose a random int and run a game associated with the int.
    randomInt = random.randint(0, index - 1)

    if randomInt == numberGuessIndex:
        print("Running Guess the Number:\n")
        numberGuess.numberGuess(minValue, maxValue)
        return 0
    elif randomInt == madLibIndex:
        print("Running Mad Libs:\n")
        madlib.madlib(madLibFile)
        return 1
    elif randomInt == wyrIndex:
        print("Running Would You Rather?:\n")
        wyr.wouldYouRather(wyrFile)
        return 2
    elif randomInt == anagramIndex:
        print("Running Anagram:\n")
        anagram.anagram()
    elif randomInt == hangmanIndex:
        print("Running Hangman:\n")
        hangman.hangman(hangmanFile)
        return 3
    else:
        # Program should never reach here.
        print("No game was found.")
        return -2
