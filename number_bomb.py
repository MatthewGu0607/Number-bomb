import random

def numberBomb():
    #Initializing game
    numPlayers = input("How many players are there?\n")
    while not numPlayers.isdigit():
        numPlayers = input("Invalid input, please enter a number.\n")
    numPlayers = int(numPlayers)

    #the list of players
    setOfPlayers = [0] * numPlayers
    for num in range(numPlayers):
        whoIsIn = "What's player #" + str(num+1) + "'s name?\n"
        Name = input(whoIsIn)
        while (Name in setOfPlayers):
            Name = input("Name repeated, change another name, please.\n")
        setOfPlayers[num] = Name
        
    #Placing the bomb
    upperBound = input("What's the upper bound of the number bomb?\n")
    while not upperBound.isdigit():
        upperBound = input("Invalid input, please enter a number.\n")
    hi = int(upperBound)
    lo = 1
    bomb = random.randint(lo,hi)
    print("Bomb created! Let's start the game ~~~")

    #Starting the game
    end = False
    while not end:
        #players choose their numbers
        for player in setOfPlayers:
            curr = 0
            while curr < lo or curr > hi:
                reInput = (player + ", Please enter a number within the range " 
                        + str(lo) + " and " + str(hi) + "\n")
                tempCurr = input(reInput)
                while not tempCurr.isdigit():
                    tempCurr = input("Invalid input, please enter a number.\n")
                curr = int(tempCurr)
            if curr == bomb:
                print("Boom", player, "you step on the bomb!\nGame is over!")
                end = True
                break
            elif bomb > curr: lo = curr + 1
            else: hi = curr - 1

numberBomb()