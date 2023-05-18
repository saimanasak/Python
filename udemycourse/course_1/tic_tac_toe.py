'''
Create a Tic Tac Toe game.
Here are the requirements:
    2 players should be able to play the game (both sitting at the same computer)
    The board should be printed out every time a player makes a move
    You should be able to accept input of the player position and then place a symbol on the board

'''

#Imported to modules random and sys:
import random
import sys

#Colors initialization and declaration:
#Used ANSI escape codes:
Red = '\033[31m'
End = '\033[m'
Cyan = '\033[36m'
Yellow = '\033[33m'
Green = '\033[32m'
Blue = '\033[34m'
Purple = '\033[35m'
Pink = '\033[95m'

def tic_tac_toe():
    
    #Introduction to game:
    print('\n')
    print(Pink + """                             ****** Welcome to Tic-Tac-Toe ******                       
          
          First, randomly a player is selected to make their selection of symbols - 'O' or 'X'
          ALternatively, players get chances to place their symbols in the 3*3 grid.
          If same symbol matches vertically, horizontally, or diagonally --> then the owner of that symbol becomes the winner.
          And the game ends.
          
          Here, you go......Game Starts now... All The Best ;)
          
          """, End)
    
    #Random player, empty board and used_positions empty list are initialized and declared:
    symbol = random.randint(1, 2)
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    used_positions = []
    
    #Prints the randomly selected player:
    print(Yellow + f"Player {symbol} gets the first chance to select their symbol.\n", End)

    #Function to display the updated board:
    def displayBoard(a):
        print('-------------------')
        print('|  ' + get_color(a[0]) + a[0] + End + '  |  ' + get_color(a[1]) + a[1] + End  + '  |  ' + get_color(a[2]) + a[2] + End  + '  |  ')
        print('-------------------')
        print('|  ' + get_color(a[3]) + a[3] + End + '  |  ' + get_color(a[4]) + a[4] + End  + '  |  ' + get_color(a[5]) + a[5] + End  + '  |  ')
        print('-------------------')
        print('|  ' + get_color(a[6]) + a[6] + End + '  |  ' + get_color(a[7]) + a[7] + End  + '  |  ' + get_color(a[8]) + a[8] + End  + '  |  ')
        print('-------------------') 
        print('\n')
    
    #Function to display alternate color for both the players' symbols:
    def get_color(token):
        if token == 'X':
            return Blue
        elif token == 'O':
            return Yellow
        else:
            return End   
    
    #Based on the random selection the player selects their symbol:   
    if symbol == 1:
        player1 = input("Hey, Player-1! You got chance to select a symbol, select a symbol 'O' or 'X': ")
        print('\n')
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        
    else:
        player2 = input("Hey, Player-1! You got chance to select a symbol, select a symbol 'O' or 'X': ")
        print('\n')
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
     
    #Prints the final symbols of the players:   
    print(f"Player 1's symbol: {player1}")
    print(f"Player 2's symbol: {player2} \n")
    
    
    #Function for player1 to place the values in desired positions:
    def player_1():
        position1 = int(input("Player1 turn, Enter a position (1 - 9) to place your symbol: "))
        print('\n')
        if position1 not in used_positions:
            used_positions.append(position1)
            board[position1-1] = player1
            displayBoard(board)
        else:
            print(Red + "Position is already filled, please select another position!! \n",End)
            player_1()
    
    #Function for player1 to place the values in desired positions:       
    def player_2():
        position2 = int(input("Player2, Enter a position (1 - 9) to place your symbol: "))
        print('\n')
        if position2 not in used_positions:
            used_positions.append(position2)
            board[position2-1] = player2
            displayBoard(board)
        else:
            print(Red + "Position is already filled, please select another position!! \n",End)
            player_2()
    
    #Function to check the winner after every player's turn:        
    def check_winner():
        if board[0] == board[1] == board[2] == 'X' or board[0] == board[1] == board[2] == 'O':
            if board[0] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
                
        elif board[3] == board[4] == board[5] == 'X' or board[3] == board[4] == board[5] == 'O':
            if board[3] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
        
        elif board[6] == board[7] == board[8] == 'X' or board[6] == board[7] == board[8] == 'O':       
            if board[6] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
        
        elif board[0] == board[4] == board[8] == 'X' or board[0] == board[4] == board[8] == 'O':
            if board[0] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
    
        elif board[2] == board[4] == board[6] == 'X' or board[2] == board[4] == board[6] == 'O':
            if board[2] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
        
        elif board[0] == board[3] == board[6] == 'X' or board[0] == board[3] == board[6] == 'O':
            if board[0] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
        
        elif board[1] == board[4] == board[7] == 'X' or board[1] == board[4] == board[7] == 'O':
            if board[1] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)
        
        elif board[2] == board[5] == board[8] == 'X' or board[2] == board[5] == board[8] == 'O':
            if board[2] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            game_winner(winner)    
                
        else:
            print(Cyan + "Still there's a chance! So, continue the game...", End)
            print('\n')
    
    #Function to decide the winner:        
    def game_winner(winner):
            if player1 == 'X' and winner == 'X':
                print(Green + "------GAME OVER------\n", End)
                print(Green + "CONGRATS! Player 1 is the winner :) \n", End)
                sys.exit()
            else:
                print(Green + "------GAME OVER------\n", End)
                print(Green + "CONGRATS! Player 2 is the winner :) \n", End)
                sys.exit()
    
    #Loop to take inputs of each player alternatively:            
    while(True):
        
        if len(used_positions) < 9:
            player_1()
            check_winner()
                        
            player_2()
            check_winner()
            
        else:
            print(Red + "------GAME OVER------\n", End)
            print(Yellow + "Board is filled, it's a tie...\n", End)
            break
        
tic_tac_toe()
