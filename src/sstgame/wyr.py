from madlib import readText
import random

def wouldYouRather(fileName):
    result = readText(fileName)
    prompt = random.choice(result)
    print(prompt)
    input("Please enter Yes or No")
