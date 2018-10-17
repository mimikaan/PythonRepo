#importing random library
import random
#make the set of moves
moves = ["rock","paper","scissors"]
keep_playing = "True"

while keep_playing == "True":
    cmove = random.choice(moves)
    pmove = input("What is your move: rock , paper or scissors?")
    print("computer chose ",cmove)
    if cmove == pmove:
        print("Tie")
    elif pmove=="rock" and cmove == "scissors":
        print("player Wins")
    elif pmove == "rock" and cmove == "paper":
        print("computer wins")
    elif pmove == "paper" and cmove =="scissors":
        print("computer wins")
    elif pmove == "paper" and cmove == "rock":
        print ("player wins")
    elif pmove == "scissors" and cmove =="rock":
        print("computter wins")
    elif pmove == "scissors" and cmove =="paper":
        print ("Player wins")  


