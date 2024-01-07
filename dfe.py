#!/usr/bin/env python
# import random module
from random import randint

# print game description and rules on screen 

print('''
        You are a candidate for Senate in the great Rainbow State of Queerty, 
        where dismal voter turnout and apathy has led to a winner-take-all 
        dildo vs fleshlight vs e-stim showdown. To win the election, 
        you must beat your opponent, Bastard Child, 
        in 3 out of 5 rounds of the beloved gayborhood game. The rules are simple. 
        On the count of 3, you and your opponent must place on the hanky a dildo, 
        fleshlight or e-stim device. Dildo beats fleshlight, fleshlight beats e-stim, 
        and e-stim beats dildo. 
        Good luck. May the rainbow shine bright and wet.
      ''')

TOYS = ["Dildo", "Fleshlight", "Electic-Stimulation"]

cpu = 0
player = 0
game_play = True

while game_play:
    cpuchoice_int = randint(0,2)
    cpuchoice = TOYS[cpuchoice_int]
    pchoice_int = None     
    while pchoice_int not in range(len(TOYS)):
        pchoice = input("Choose your device\n[0 = Dildo, 1 = Fleshlight, 2 = E-Stim]: ")
        try:
            pchoice_int = int(pchoice)
        except:    
            print("must enter integer* for valid device!\n")
    print(f"\nPlaying You:{TOYS[pchoice_int]} vs Opponent:{cpuchoice}\n")

    if (pchoice_int - cpuchoice_int) in (-1,2):
        y = "win"
        print("Nailed it!\n") 
    elif (pchoice_int - cpuchoice_int) == 0:
        y = "tie"
        print("power-puff draw!\n")
    else:
        y = "loose"
        print("You dropped the soap!\n")
    
    if y == "win":
        player +=1
        print(f"Player:{player} and Opponent:{cpu}\n")        
    elif y == "loose":
        cpu +=1
        print(f"Player:{player} and Opponent:{cpu}\n")
    else:
        print(f"Player:{player} and Opponent:{cpu}\n")
        
    if cpu == 3:
        print("Sashay-away my dear!...Better luck next gay-lection")
        break
    elif player == 3:
        print("Congrats..You are now a Royal Queen of Queerty")
        break


