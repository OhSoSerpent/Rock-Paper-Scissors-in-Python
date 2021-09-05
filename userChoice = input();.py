from random import *
from typing import Container
games = ["1. Rock Paper Scissors"];
willToPlay = 1;
currentGame = None;
def rps(): 
    comp = ["Rock", "Paper", "Scissors"];
    finalChoice = "";
    rand = randint(1,3);
    playerNum = None;
    compNum = None;
    print("Let's play Rock Paper Scissors!");
    userChoice = input("Choose: ");
    choice = userChoice.lower();
    #This chunk handles the user input
    if choice == "rock":
        playerNum = 0;
    elif choice == "paper":
        playerNum = 1;
    elif choice == "scissors":
        playerNum = 2;
    else : print("Read Carefully");
    #This chunk handles the computers choice
    if rand == 1:
        finalChoice = "Rock";
    elif rand == 2:
        finalChoice = "Paper";
    else: finalChoice = "Scissors";
    if finalChoice == "Rock":
        compNum = 0;
    elif finalChoice == "Paper":
        compNum = 1;
    else: compNum = 2;
    print("You chose " + choice);
    print("Computer chose " + finalChoice);
    #This determines the games outcome
    print(playerNum);
    print(compNum);
    if choice == "rock" and finalChoice == "Scissors" :
        print("You Win!");
    elif choice == "scissors" and finalChoice == "Rock" :
        print("You Lost");
    elif choice == "rock" and finalChoice == "Scissors" :
        print("You win!")
    elif playerNum - compNum == 0:
        print("Tie Game!");
    elif playerNum - compNum > 0:
        print("You win");
    elif playerNum - compNum < 0:
        print("You lost!");
    else: print("Tie game");
while willToPlay == 1:
    print("What do you want to play?")
    print(games);
    game= input("Choose: ");
    game.lower();
    if game == "1":
        rps();
        currentGame = rps;