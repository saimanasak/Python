
Red = '\033[31m'
End = '\033[m'
Cyan = '\033[36m'
Yellow = '\033[33m'
Green = '\033[32m'
Blue = '\033[34m'
Pink = '\033[95m'

def adventure_game():
    
    print(Yellow + '''
            *******************************************************************************
                    |                   |                  |                     |
            _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                    |                `"=._o`"=._      _`"=._                     |
            _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                    |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
            _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
        ''', End)
    
    print(Cyan + "Welcome to Treasure Island", End)
    
    path = input("""\nYou're at a crossroad. 
                 Where do you want to go? 
                 Type 'left' or 'right': """)
    if path.lower() == "left":
        action = input("""\n
                       You've come to a lake. 
                       There is an island in the middle of the lake.
                       Type 'wait' to wait for a boat. Type 'swim' to swim across: """)
        if action.lower() == "wait":
            color = input("""\n
                          You arrive at the island unharmed. 
                          There is a house with 3 doors. 
                          One RED, one YELLOW and one BLUE. 
                          Which colour do you choose?: """)
            if color.lower() == "red":
                print(Red + """\n
                      It's a room full of fire... 
                      Game Over!""", End)
            elif color.lower() == "yellow":
                print(Green + """\n
                      You found the treasure... 
                      You Win!""", End)
            elif color.lower() == "blue":
                print(Red + """\n
                      You entered a room of beasts... 
                      Game Over!""", End)
            else:
                print(Red + """\n
                      You chose a door that doesn't exist...
                      Game Over!""", End)
        elif action.lower() == "swim":
            print(Red + """\n
                  You got attacked by an angry trout...
                  Game Over!""", End)
        else:
            print(Red + """\n
                  Wrong action...
                  Game Over!""", End)
    elif path.lower() == "right":
        print(Red + """\n
              You fell into a hole...
              Game Over!""", End)
    else:
        print(Red + """\n
              Wrong direction...
              Game Over!""", End)
        
adventure_game()
