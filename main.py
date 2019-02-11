import time

print("Welcome to Rock, Paper, scissor 2 players game by Nyrroz. " "\n \n")

def result(playerOne, playerTwo):
if playerOne == playerTwo:
print("Equality !")

```
elif int(playerOne == 1) and int(playerTwo == 2):
    print("The paper covers the rock","\n The player 2 wins !")

elif int(playerOne == 1) and int(playerTwo == 3):
    print("Rock destroy Scissors", "\n The player 1 won !")

elif int(playerOne == 2) and int(playerTwo == 1):
    print("The paper covers the rock","\n The player 1 wins !")

elif int(playerOne == 2) and int(playerTwo == 3):
    print("The scissors cut the paper","\n The player 2 wins !")

elif int(playerOne == 3) and int(playerTwo == 1):
    print("The scissors are destroyed by the rock","\n The player 2 wins !")

elif int(playerOne == 3) and int(playerTwo == 2):
    print("The scissors cut the paper","\n The player 1 wins !")



elif int(playerOne == 3) and int(playerTwo == 1):
    print("Rock destroy Scissors", "\n The player 2 won !")



return
```
def playAgainFunction():

```
playAgain = input("Play Again ? (type \"Y/N\": ")
playAgain = str(playAgain)
if str(playAgain) == "Y":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    newGame()
elif str(playAgain) == "y":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    newGame()
elif str(playAgain) == "yes":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    newGame()
elif str(playAgain) == "n":
    print("Thanks for playing, see you soon :p")
    time.sleep(2)
    game = False
elif str(playAgain) == "N":
    print("Thanks for playing, see you soon :p")
    time.sleep(2)
    game = False
elif str(playAgain) == "no":
    print("Thanks for playing, see you soon :p")
    time.sleep(2)
    game = False
else:
    print("ERROR, please type \"yes\" or \"no\" ")
    playAgainFunction()
```
def newGame(): #Game function

```
playerOne = input("Player 1, it is your turn, choose between: \n1- Rock \n2- Paper \n3- Scissors \n---> ")
playerOne = int(playerOne)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
playerTwo = input("Player 2, it is your turn, choose between: \n1- Rock \n2- Paper \n3- Scissors \n---> ")
playerTwo = int(playerTwo)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
result(playerOne, playerTwo)
playAgainFunction()
```
game = True
while game :

```
runGame = input("Type \"START\" to start a new game: ")
runGame = str(runGame)
if runGame == str("start"):
    print("New game... \n \n")
    newGame()

    break
elif runGame ==str("START"):
    print("New game... \n \n")
    newGame()

    break
else:
    pass
```
