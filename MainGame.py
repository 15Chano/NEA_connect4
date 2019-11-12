#fstrings
#do when game draws
#slot full 
"""Generates The Board"""
def board(row):
    board1=[]
    for i in range(0,row):
        board1.append([0,0,0,0,0,0,0])
    return board1

def printboard(gameboard): # prints the current board
    for i in range(0,6):
        print(gameboard[i])

"""User Inputs"""
def user_input1():  # verifies correct userinput for the game
    while True:
        input1 = int(input("Player 1 Column Number:"))
        if input1 < 1 or input1> 7:
            print("Try Again, Numbers Can Only Be 1,2,3,4,5,6,7")
            pass
        else:
            return input1
            break
def user_input2():
    while True:
        input2 = int(input("Player 2 Column Number:"))
        if input2 < 1 or input2> 7:
            print("Try Again, Numbers Can Only Be 1,2,3,4,5,6,7")
            pass
        else:
            return input2
            break
""" Board Updaters """      
def board_updater1(player_input1,gameboard): #changes to 0's to 1's
    for i in range(0,5):
        if gameboard[i+1][player_input1-1] == 0:
            gameboard[i][player_input1-1] = 0
        else:
            if gameboard[i+1][player_input1-1] == 1 or 2:
                gameboard[i][player_input1-1] = 1
                break
    if gameboard[5][player_input1-1] == 0:
        gameboard[5][player_input1-1] = 1

    return gameboard

def board_updater2(player_input2,gameboard):   
    for i in range(0,5):
        if gameboard[i+1][player_input2-1] == 0:
            gameboard[i][player_input2-1] = 0
        else:
            if gameboard[i+1][player_input2-1] == 1 or 2:
                gameboard[i][player_input2-1] = 2
                break
    if gameboard[5][player_input2-1] == 0:
        gameboard[5][player_input2-1] = 2
    
    return gameboard

"""checking For Win Condition"""
def win_condition_checker(gameboard):
    
    game = None
    
    def horizontal(gameboard):
        for i in range(0,6): # i= row number h = placement in row i 
            for h in range(0,4):
                if gameboard[i][h] == 1  and gameboard[i][h+1] == 1 and gameboard[i][h+2] == 1 and gameboard[i][h+3] == 1:
                    print("Player 1 Wins")
                    return 1
                if gameboard[i][h] == 2 and gameboard[i][h+1] == 2 and gameboard[i][h+2] == 2 and gameboard[i][h+3] == 2:
                    print("Player 2 Wins")
                    return 1

    def verticle(gameboard):
        for i in range(0,3): # i=row number  h = placement in row i 
            for h in range(0,7):
                if gameboard[i][h] == 1 and gameboard[i+1][h] == 1 and gameboard[i+2][h] == 1 and gameboard[i+3][h] == 1:
                    print("Player 1 Wins")
                    return 1
                if gameboard[i][h] == 2 and gameboard[i+1][h] == 2 and gameboard[i+2][h] == 2 and gameboard[i+3][h] == 2:
                    print("Player 2 Wins")
                    return 1 
    
    def diagonal_ne(gameboard): # i = row number h = placement in row i 
        for i in range(4,6):
            for h in range(0,4):
                if gameboard[i][h] == 1 and gameboard[i-1][h+1] == 1 and gameboard[i-2][h+2] == 1 and gameboard[i-3][h+3] == 1:
                    print("Player 1 Wins")
                    return 1 
                if gameboard[i][h] == 2 and gameboard[i-1][h+1] == 2 and gameboard[i-2][h+2] == 2 and gameboard[i-3][h+3] == 2:
                    print("Player 2 Wins")
                    return 1 
    
    def diagonal_nw(gameboard):
        for i in range(4,6):
            for h in range(0,4):
                if gameboard[i][h] == 1 and gameboard[i-1][h-1] == 1 and gameboard[i-2][h-2] == 1 and gameboard[i-3][h-3] == 1:
                    print("Player 1 Wins")
                    return 1 
                if gameboard[i][h] == 2 and gameboard[i-1][h-1] == 2 and gameboard[i-2][h-2] == 2 and gameboard[i-3][h-3] == 2:
                    print("Player 2 Wins")
                    return 1 
                
        
    test1 = horizontal(gameboard)
    test2 = verticle(gameboard)
    test3 = diagonal_ne(gameboard)
    test4 = diagonal_nw(gameboard)
    if test1 == 1 or test2 == 1 or test3 == 1 or test4 == 1:
        game = True
        return game
             

"""Main Fuction The Gameloop"""        
def main():
    game_condition = False 
    row = 6 
    gameboard = board(row) # generates lists of 000000
    while not game_condition:
        player_input1 = user_input1() # gets the user input 
        gameboard=board_updater1(player_input1,gameboard) #changing 0 to 1 
        printboard(gameboard)
        game_condition = win_condition_checker(gameboard)
        if game_condition:
            break
        player_input2 = user_input2()
        gameboard = board_updater2(player_input2,gameboard)
        printboard(gameboard)
        game_condition = win_condition_checker(gameboard)
        
        
        
       
main()
