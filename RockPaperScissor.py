# We Have to make Rock-paper-Scissor Game
""" Steps ->>>
    1.Your choice 
    2.Computer choice (random choice)
    3.Winner's name

    Logic ->>

    ---Rock---
    Rock-Rock = match draw
    Rock-Paper = Paper Win
    Rock-Scissor = Rock win

    ---Paper---
    Paper-Paper= match draw
    Paper-Rock = Paper Win
    Paper-Scissor = Scissor win

    ---Scissor---
    Scissor-Scissor= match draw
    Scissor-Rock = Rock Win
    Scissor-Paper = Scissor win
"""

print("ROCK-PAPER-SCISSOR GAME")
import random       #imported random to make random choice
items=["Rock","Paper","Scissor"]

user_choice=input("Enter your move: Rock,Paper,Scissor = ")
comp_choice=random.choice(items)

print(f"User choice ={user_choice} , Computer choice={comp_choice}")

if user_choice == comp_choice:
    print("Match draw")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper wrap Rock : Computer Win!!" )
    else:
        print("Rock destroy scissor : You Win!!")

elif user_choice=="Paper":
    if comp_choice=="Rock":
        print("Paper wrap Rock : You Win!!" )
    else:
        print("Scissor cuts paper : Computer Win!!")
        
elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor cuts Paper : You Win!!" )
    else:
        print("Rock destroy scissor : Computer Win!!")

