def info(help = False, list = False):
    if(help == True and list == True):
        return
    if(help == True):
        print("Here are the commands to run the games")
        print("Run ")
    if(list == True):
        print("This is our list of games")
        print("1. Madlibs")
        print("2. Guess the Number")
        print("3. Would You Rather")
        print("4. Random Game")
