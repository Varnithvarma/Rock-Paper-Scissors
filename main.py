from random import randint
t = ["Rock","Paper","Scissor"]
Computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock,Paper,Scissor:\n")
    if player == Computer:
        print("Tie")
    elif player =="Rock":
        if Computer =="Paper":
            print("You Lose!", Computer, "Covers", player)
        else:
            print("You Win!",player,"smashes",Computer)
    elif player == "Paper":
        if Computer == "Scissors":
            print("You Lose!",Computer,"Cut",player)
        else:
            print("You win!",player,"covers",Computer)
    elif player =="Scissor":
        if Computer == "Rock":
            print("You lose.",Computer,"smashes",player)
        else:
            print("You Win!",player,"cut",Computer)

    else:
        print("Error Try again")
    player = False
    Computer = t[randint(0,2)]


