#This is the final version of the game
#updated rock paper scissors game now has 12 options enter options using letters as your input.
#all avalible options
#r=rock
#p=paper
#s=scissors
#l=lightsaber
#b=blaster
#i=ion grenade
#w=wolf
#h=human
#g=goblin
#a=air
#f=fire
#e=earth
#Hidden in the code there is a way to get 1 free point.....you may need it but its up to you to figure it out.

#Instructions for Running my Project
#step 1 open a new file on python
#step 2 select run module from the options menu
#step 3 enjoy!

import random
choicelist = ["Rock", "Paper", "Scissors","lightsaber","blaster","ion grenade","wolf","human","goblin","air","fire","earth"]
wins = 0
losses = 0
run = True
while run == True:
    user_input = input(str("r for rock, p for paper, and s for scissors.\n"))
    if user_input == "r":
        user_input = 0
    elif user_input == "p":
        user_input = 1
    elif user_input == "s":
        user_input = 2
    elif user_input == "l":
        user_input = 3
    elif user_input == "b":
        user_input = 4
    elif user_input == "i":
        user_input = 5
    elif user_input == "w":
        user_input = 6
    elif user_input == "h":
        user_input = 7
    elif user_input == "g":
        user_input = 8
    elif user_input == "a":
        user_input = 9
    elif user_input == "f":
        user_input = 10
    elif user_input == "e":
        user_input = 11
    else:
        print("Please enter a valid choice.")
        if user_input == "joust":
            wins = wins + 1
            continue
           
    comp_input = random.randint(0, 11)
    print(choicelist[user_input], "vs.", choicelist[comp_input])
    if user_input == comp_input:
        print("Joust.")
        losses += -1
    elif ((user_input - comp_input + 3) % 3 == 1):
        print("Win.")
        wins = wins + 1
    else:
        print("Lose.")
        losses += 1
    print("Player: ", wins, "\nComputer: ", losses)
    again = True
    while again == True:
        playagain = input(str("Play again (y or n)? "))
        if playagain == "n":
            print("Goodbye!")
            run = False
            again = False
        elif playagain == "y":
            print("Let's play again.")
            again = False
        else:
            print("Please enter a valid choice.")
            continue
