from src.sstgame.madlib import readText
import random
import os


def wouldYouRather(fileName = None):
    if fileName is None:
        package_dir = os.path.dirname(__file__)
        fileName = os.path.join(package_dir, "wyr.txt")
    result = readText(fileName)
    prompt = random.choice(result)
    print(prompt)
    input("Please enter Yes or No")
