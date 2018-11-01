from random import randint

#  available weapons => stored in an array
#  choices numbers 0, 1, 2
choices = ["Rock", "Paper", "Scissors"]
player = False
# starting lives
computerLife = 3
playerLife = 3
# restarting the game
restart = ["Y", "N"]
# making the computer pick one item at random
computer = choices[randint(0,2)]

# user choice
while player is False: 
    player = input("Choose: Rock, Paper or Scissors?").capitalize()
    print("Player chooses:", player)
# showing the computers choice in the terminal window
    print("Computer Chooses:", computer)

# check for equal values
    if (player == computer):
        print("It's a tie!")

# player picks Rock
    elif (player == "Rock"):
        if (computer == "Paper"):
            # computer wins "paper covers rock
            playerLife -= 1
            print("Computer Wins", computer, "covers", player, ".")
            print("You have", playerLife, "lives left.")
        else:
            # player wins "rock smashes scissors"
            computerLife -= 1
            print("You Win!", player, "smashes", computer)
            print("The computer has", computerLife, "lives left.")

# player picks paper
    elif (player == "Paper"):
        if (computer == "Scissors"):
            # computer wins "scissors cut paper"
            playerLife -= 1
            print("Computer Wins. You Lose!", computer, "cuts", player)
            print("You have", playerLife, "lives left.")
        else:
            #  player wins "paper covers rock"
            computerLife -= 1
            print("You Win! Computer Loses!", player, "covers", computer)
            print("The computer has", computerLife, "lives left.")
# player picks scissors
    elif (player == "Scissors"):
        if (computer == "Rock"):
            # computer wins "Rock smashes scissors"
            playerLife -= 1
            print("Computer Wins. You Lose!", computer, "smashes", player)
            print("You have", playerLife, "lives left.")
        else:
            # player wins "Scissors cut paper"
            computerLife -= 1
            print("You Win! Computer Loses!", player, "cuts", computer)
            print("The computer has", computerLife, "lives left.")
# unknown entries
    else:
        print("Please select a valid option")

    # reset counter
    player = False
    computer = choices[randint(0,2)]

    # tracking lives
    if (computerLife == 0):
        print("You have won! The computer is out of lives!")
        restart = input("Would you like to play again? Y / N ").capitalize()

    if (playerLife == 0):
        print("You have 0 lives left. The computer has won!")
        restart = input("Would you like to play again? Y / N ").capitalize()

     # restarting the game
    if (restart == "Y"):

    if (restart == "N"):
        quit()