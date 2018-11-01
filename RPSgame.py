from random import randint

#  available weapons => stored in an array
#  choices numbers 0, 1, 2
choices = ["Rock", "Paper", "Scissors"]
player = False
replay = True
# lives counter
playerLife = 5
computerLife = 5

# making the computer pick one item at random
computer = choices[randint(0,2)]

while player is False:
    print("**********************************************************")
    print("Player Lives:", playerLife, "/5\n")
    print("Computer Lives:", computerLife, "/5\n")
    print("Type 'Quit' to exit the game at any point.\n")
    print("**********************************************************")
    player = input("Choose: Rock, Paper or Scissors?\n").capitalize()
    
# check for equal values
    if (player == computer):
        print("It's a tie!\n")

# player picks Rock
    elif (player == "Rock"):
        if (computer == "Paper"):
            # computer wins "paper covers rock
            playerLife -= 1
            print("Computer Wins", computer, "covers", player, ".\n")
        else:
            # player wins "rock smashes scissors"
            computerLife -= 1
            print("You Win!", player, "smashes", computer, "!\n")

# player picks paper
    elif (player == "Paper"):
        if (computer == "Scissors"):
            # computer wins "scissors cut paper"
            playerLife -= 1
            print("Computer Wins. You Lose!", computer, "cuts", player, "!\n")
        else:
            #  player wins "paper covers rock"
            computerLife -= 1
            print("You Win! Computer Loses!", player, "covers", computer, "!\n")
# player picks scissors
    elif (player == "Scissors"):
        if (computer == "Rock"):
            # computer wins "Rock smashes scissors"python3 
            playerLife -= 1
            print("Computer Wins. You Lose!", computer, "smashes", player, "!\n")
        else:
            # player wins "Scissors cut paper"
            computerLife -= 1
            print("You Win! Computer Loses!", player, "cuts", computer, "!\n")

    elif (player == "Quit"):
        print("*******************************************************")
        print("Thanks for playing!!")
        print("*******************************************************\n")
        exit()

# unknown entries
    else:
        print("Please select a valid option\n")

#win or lose check
    if playerLife == 0 or computerLife == 0:
            if playerLife == 0:
                replay = False
                print("YOU LOST!\n")
            else:
                print("YOU WIN!!\n")
                replay = False
    while replay is False:
        print("**********************************************************")
        print("Would you like to play again?")
        print("**********************************************************")
        replay = input("Y / N").capitalize()
# resetting stats
        if replay == "Y":
            playerLife = 5
            computerLife = 5
            player = False
            computer = choices[randint(0,2)]
        else:
            print("*******************************************************")
            print("Thanks for playing!!")
            print("*******************************************************\n")
            exit()


    # reset counter
    player = False
    computer = choices[randint(0,2)]
