# Python Code for Swim Or Drown Card Game
# Swim Or Drown Cards Work In Progress: Prints Each Player's Cards
import sys, os, array, time, random

class PCard(): # Play cards.
    def __init__(self, type, value):
        self.type = type # type: number or wild
        self.value = value # value: 0-9 or name of any wild card.

class Player():
    def __init__(self, PCD, FCN, drown):
        self.PCD = PCD # playcard deck: Array of play cards.
        self.FCN = FCN # Float card number: Number of float tokens.
        self.drown = drown # Drown is true or false. Determines whether player is out or not.

stack = []
P = []
swim = 2

def init():
    print("Sink Or Drown - Card Game")
    print("Made by Rishi Prasanna, Junior at UCSC")
    defPCards()
    shuffleCards()
    while True:
        s = input("New game? y/n: ")
        if s == "y":
            beginGame()
        else:
            break



def beginGame():
    n = "2"
    num = 2
    while True:
        n = input("How many players? ")
        try:
            num = int(n)
        except TypeError:
            print("Error: Must type a number that >= 2 and <= 5!")
            continue

        if num == 1:
            print("Error: This is a multiplayer game! Must be 2 to 5!")
        elif num < 2 or num > 5:
            print("Error: Must be 2 to 5!")
        else:
            break

    defPlayers(num)

    shuffleCards()
    while True:
        print("Cards shuffled.")
        s = input("Shuffle again? y/n: ")
        if s == "y":
            shuffleCards()
        else:
            break

    distCards()
    GIP()
    # PAIS()


"""
So here's how this is going to work.
There will be:
3 of each number card, 0 to 9.
So 30 number cards.
8 Current.
8 Reverse.
7 Wheel.
9 Small Bait.
7 Big Bait.
10 Bubbles.
7 Fish.
5 Sea Turtle.
3 Dolphin.
1 Whale.
10 Seaweed.
9 Octopus.
7 Shark.
5 Crocodile.
"""



def defPCards():
    # All number cards.
    for x in range(0,10):
        for y in range(1,4):
            C = PCard(str(x), "number")
            stack.append(C)

    # All wild cards.
    # :)
    for a in range(1,9):
        W = PCard("current", "wild")
        stack.append(W)

    # :)
    for b in range(1,9):
        W = PCard("reverse", "wild")
        stack.append(W)

    # :)
    for c in range(1,8):
        W = PCard("wheel", "wild")
        stack.append(W)

    # :)
    for d in range(1,10):
        W = PCard("small bait", "wild")
        stack.append(W)

    # :)
    for e in range(1,8):
        W = PCard("big bait", "wild")
        stack.append(W)

    # :)
    for f in range(1,11):
        W = PCard("bubbles", "wild")
        stack.append(W)

    # :)
    for g in range(1,8):
        W = PCard("fish", "wild")
        stack.append(W)

    # :)
    for h in range(1,6):
        W = PCard("sea turtle", "wild")
        stack.append(W)

    # :)
    for i in range(1,4):
        W = PCard("dolphin", "wild")
        stack.append(W)

    # :)
    for j in range(1,2):
        W = PCard("whale", "wild")
        stack.append(W)

    # :)
    for k in range(1,11):
        W = PCard("seaweed", "wild")
        stack.append(W)

    # :)
    for l in range(1,10):
        W = PCard("octopus", "wild")
        stack.append(W)

    # :)
    for m in range(1,8):
        W = PCard("shark", "wild")
        stack.append(W)

    # :)
    for n in range(1,6):
        W = PCard("crocodile", "wild")
        stack.append(W)
    return

def shuffleCards(): # Shuffles cards using Fisher-Yates algorithm.
    for i in range(len(stack) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)

        # Swap arr[i] with the element at random index
        stack[i], stack[j] = stack[j], stack[i]
    return

def defPlayers(numPlayers): # Argument: number of players
    for x in range(0, numPlayers):
        PL = Player([], 5, False)
        P.append(PL)
    return

def resetPlayers():
    P = []
    return

def PAIS(): # Print All cards In Stack.
    print("")
    for C in stack:
        print(C.type + " card: " + C.value)
    print("")
    return


def distCards():
    # Each player gets five play cards.
    for y in range(0, len(P)):
        for x in range(0, 5):
            C = stack.pop()
            # print(C.type + " card: " + C.value)
            P[y].PCD.append(C)
    return

def DCFS(): # Draw Card From Stack.
    C = stack.pop()
    return C

def PCBIS(C): # Put Card Back In Stack.
    stack.insert(0, C)
    return

def printPCD(x):
    print("")
    player = P[x]
    for C in player.PCD:
        print(C.type + " card: " + C.value)
    print("")
    return

def GIP():
    # First, the opening card. This determines sink/swim.
    # If even, then evens are swim and odds are sink.
    # If odd, then odds are swim and evens are sink.
    # If wild, put the card back in the stack and draw again until you get an even or odd.
    for y in range(0, len(P)):
        print("\nPlayer " + str(y+1) + "\'s deck:")
        printPCD(y)
        input("Press Enter to continue\n")
    return


try:
    init()
except KeyboardInterrupt:
    print("\n\nForce quit.")
finally:
    print("Exiting...")

