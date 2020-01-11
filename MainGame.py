#git add Maingame.py
#git comment -m "comment"
#git push -u origin maaster 
import random
import copy 
import math 
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
def user_input1(gameboard):  # verifies correct userinput for the game
    while True:
        input1 = int(input("Player 1 Column Number:"))
        if input1 < 1 or input1> 7:
            print("Try Again, Numbers Can Only Be 1,2,3,4,5,6,7")
            pass
        else:
            pass
#bellow checks if the column is full        
        if input1 == 1:
            column1 =[]
            for i in range(0,6):
                column1.append(gameboard[i][0])
            if 0 not in column1:
                print("Column 1 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
        
        if input1 == 2:
            column2 = []
            for i in range(0,6):
                column2.append(gameboard[i][1])
            if 0 not in column2:
                print("Column 2 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
        
        if input1 == 3:
            column3 = []
            for i in range(0,6):
                column3.append(gameboard[i][2])
            if 0 not in column3:
                print("Column 3 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
            
        if input1 == 4:
            column4 = []
            for i in range(0,6):
                column4.append(gameboard[i][3])
            if 0 not in column4:
                print("Column 4 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
            
        if input1 == 5:
            column5 = []
            for i in range(0,6):
                column5.append(gameboard[i][4])
            if 0 not in column5:
                print("Column 5 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
            
        if input1 == 6:
            column6 = []
            for i in range(0,6):
                column6.append(gameboard[i][5])
            if 0 not in column6:
                print("Column 6 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
        
        if input1 == 7:
            column7 = []
            for i in range(0,6):
                column7.append(gameboard[i][6])
            if 0 not in column7:
                print("Column 7 Full Select, Please Select Another Column")
                pass
            else:
                return input1
                break
          
            
def user_input2(gameboard):
    while True:
        input2 = int(input("Player 2 Column Number:"))
        if input2 < 1 or input2> 7:
            print("Try Again, Numbers Can Only Be 1,2,3,4,5,6,7")
            pass
        else:
            pass
        for i in range(1,8):
            if input2 == i:
                column1 = []
                for h in range(0,6):
                    column1.append(gameboard[h][0])
                if 0 not in column1:
                    print("Column" + i + "Full Select, Please Select Another Column")
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
        if gameboard[i+1][player_input2] == 0:
            gameboard[i][player_input2] = 0
        else:
            if gameboard[i+1][player_input2] == 1 or 2:
                gameboard[i][player_input2] = 2
                break
    if gameboard[5][player_input2] == 0:
        gameboard[5][player_input2] = 2
    
    return gameboard

"""checking For Win Condition"""
def ai_win(gameboard):
    def horizontal(gameboard):
        for i in range(0,6): # i= row number h = placement in row i 
            for h in range(0,4):
                if gameboard[i][h] == 2 and gameboard[i][h+1] == 2 and gameboard[i][h+2] == 2 and gameboard[i][h+3] == 2:
                    return 1
    def verticle(gameboard):
        for i in range(0,3):
            for h in range(0,7):
                if gameboard[i][h] == 2 and gameboard[i+1][h] == 2 and gameboard[i+2][h] == 2 and gameboard[i+3][h] == 2:
                    return 1 
    def diagonal_ne(gameboard): # i = row number h = placement in row i 
        for i in range(3,6):
            for h in range(0,4):
                if gameboard[i][h] == 2 and gameboard[i-1][h+1] == 2 and gameboard[i-2][h+2] == 2 and gameboard[i-3][h+3] == 2:
                    return 1 
    def diagonal_nw(gameboard):
        for i in range(3,6):
            for h in range(3,7):
                if gameboard[i][h] == 2 and gameboard[i-1][h-1] == 2 and gameboard[i-2][h-2] == 2 and gameboard[i-3][h-3] == 2:
                    return 1 
    test1 = horizontal(gameboard)
    test2 = verticle(gameboard)
    test3 = diagonal_ne(gameboard)
    test4 = diagonal_nw(gameboard)
    
    if test1 == 1 or test2 == 1 or test3 == 1 or test4 == 1:
        game = 2
        return game
    
def player_win(gameboard):
    def horizontal(gameboard):
        for i in range(0,6): # i= row number h = placement in row i 
            for h in range(0,4):
                if gameboard[i][h] == 1  and gameboard[i][h+1] == 1 and gameboard[i][h+2] == 1 and gameboard[i][h+3] == 1:
                    print("Player 1 Wins")
                    return 1
    def verticle(gameboard):
        for i in range(0,3): # i=row number  h = placement in row i 
            for h in range(0,7):
                if gameboard[i][h] == 1 and gameboard[i+1][h] == 1 and gameboard[i+2][h] == 1 and gameboard[i+3][h] == 1:
                    print("Player 1 Wins")
                    return 1
    def diagonal_ne(gameboard): # i = row number h = placement in row i 
        for i in range(3,6):
            for h in range(0,4):
                if gameboard[i][h] == 1 and gameboard[i-1][h+1] == 1 and gameboard[i-2][h+2] == 1 and gameboard[i-3][h+3] == 1:
                    print("Player 1 Wins")
                    return 1 
    def diagonal_nw(gameboard):
        for i in range(3,6):
            for h in range(3,7):
                if gameboard[i][h] == 1 and gameboard[i-1][h-1] == 1 and gameboard[i-2][h-2] == 1 and gameboard[i-3][h-3] == 1:
                    print("Player 1 Wins")
                    return 1 
    test1 = horizontal(gameboard)
    test2 = verticle(gameboard)
    test3 = diagonal_ne(gameboard)
    test4 = diagonal_nw(gameboard)
    
    if test1 == 1 or test2 == 1 or test3 == 1 or test4 == 1:
        game = 1
        return game
    
                
                
    
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
        for i in range(3,6):
            for h in range(0,4):
                if gameboard[i][h] == 1 and gameboard[i-1][h+1] == 1 and gameboard[i-2][h+2] == 1 and gameboard[i-3][h+3] == 1:
                    print("Player 1 Wins")
                    return 1 
                if gameboard[i][h] == 2 and gameboard[i-1][h+1] == 2 and gameboard[i-2][h+2] == 2 and gameboard[i-3][h+3] == 2:
                    print("Player 2 Wins")
                    return 1 
    
    def diagonal_nw(gameboard):
        for i in range(3,6):
            for h in range(3,7):
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
"""Checks If The Game Is Drew"""
def game_draw(gameboard):
    used_spaces = 0 
    for i in range(0,6):
        for h in range(0,7):
            if gameboard[i][h] == 1 or gameboard[i][h] == 2:
                used_spaces = used_spaces + 1
    return used_spaces            
"""-----------------------------------------------------------"""
"""AI / BOT For Connect Four"""
def freespace(gameboard):
    def freespace1(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][0] != 0:
                column -= 1
        return column

    def freespace2(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][1] != 0:
                column -= 1
        return column


    def freespace3(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][2] != 0:
                column -= 1
        return column


    def freespace4(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][3] != 0:
                column -= 1
        return column

    def freespace5(gameboard):
        column = 5 

        for i in range(5,-1,-1):
            if gameboard[i][4] != 0:
                column -= 1
        return column

    def freespace6(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][5] != 0:
                column -= 1
        return column

    def freespace7(gameboard):
        column = 5 
    
        for i in range(5,-1,-1):
            if gameboard[i][6] != 0:
                column -= 1
        return column
    

    a=freespace1(gameboard)
    b=freespace2(gameboard)
    c=freespace3(gameboard)
    d=freespace4(gameboard)
    e=freespace5(gameboard)
    f=freespace6(gameboard)
    g=freespace7(gameboard)
    
    freespace = [a,b,c,d,e,f,g]
    return freespace
def freespace2(freespace):
    for x,y in enumerate(freespace):
        pass
        
def scoring_position(gameboard,freespace):
    copy_board = copy.deepcopy(gameboard)
    #printboard(copy_board)
    
    
    score = 0
    
    bestmove = []
    for x,y in enumerate(freespace):
        column_cord = 0
        row_cord = 0
        copy_board[y][x] = 2
        column_cord = y 
        row_cord = x 
        #print(y,x) 
        
        #defending against diagonals 4 in a row ne
        if y < 3 and x > 2:
            if copy_board[y+1][x-1] == 1 and copy_board[y+2][x-2] == 1 and copy_board[y+3][x-3] == 1:
                score += 500
                column_cord = y 
                row_cord = x
            
        
        #defending against diaganols 4 in a row  nw
        if y < 3 and x <4:
            if copy_board[y+1][x+1] == 1 and copy_board[y+2][x+2] == 1 and copy_board[y+3][x+3] == 1:
                score += 500
                column_cord = y 
                row_cord = x
            
        
        if y < 3: #defending against vertical 4 in a row 
            if copy_board[y+1][x] == 1 and copy_board[y+2][x] == 1 and copy_board[y+3][x] == 1:
                score += 500
                column_cord = y 
                row_cord = x
        
        #2 in a row horizontal 
        if x == 0:
            #defense
            if copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1 and copy_board[y][x+3] == 1:
                score += 500
                column_cord = y 
                row_cord = x
            #attacking 
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2:#2
                score += 5 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2 and copy_board[y][x+3] == 2: #4 
                score += 1000
                column_cord = y 
                row_cord = x
                
            
        if x == 1:
            #defending
            if copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1 and copy_board[y][x+3] == 1:
                score += 500 
                column_cord = y 
                row_cord = x 
            if copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1:
                score += 500 
                column_cord = y 
                row_cord = x 
            #attacking
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
           
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
                
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x    
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x  
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2 and copy_board[y][x+3] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x  
        
        if x ==2:
            #defending
            if copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1:
                score += 500
                column_cord = y 
                row_cord = x
            if copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1 and copy_board[y][x+3] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            #attacking
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
           
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
           
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
                
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#4
                score += 1000
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2 and copy_board[y][x+3] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
        
        if x == 3:
            #defending
            if copy_board[y][x-3] == 1 and copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1:
                score += 500
                column_cord = y 
                row_cord = x
            if copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1 and copy_board[y][x+3] == 1:
                score += 500 
                column_cord = y 
                row_cord = x    
            #attacking
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
           
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
                
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2 and copy_board[y][x+3] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-3] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x
            
        if x == 4:
            #defending
            if copy_board[y][x-3] == 1 and copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1 and copy_board[y][x+2] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            #attacking 
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
           
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
    
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
                
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-3] == 2:#4
                score += 1000
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#4
                score += 1000
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x+2] == 2:#4
                score += 1000
                column_cord = y 
                row_cord = x
                
        if x == 5:
            #defending
            if copy_board[y][x-3] == 1 and copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            if copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1 and copy_board[y][x+1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            
            #attacking
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
            
           
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2: #2 
                score += 5 
                column_cord = y 
                row_cord = x
                
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x+1] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x    
            
            if copy_board[y][x] == 2 and copy_board[y][x+1] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#4
                score += 1000
                column_cord = y 
                row_cord = x  
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-3] == 2:#4
                score += 1000 
                column_cord = y 
                row_cord = x  
            
        if x == 6:
            #defending
            if copy_board[y][x-3] == 1 and copy_board[y][x-2] == 1 and copy_board[y][x-1] == 1:
                score += 500 
                column_cord = y 
                row_cord = x
            #attacking
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2:#2
                score += 5 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2:#3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y][x-1] == 2 and copy_board[y][x-2] == 2 and copy_board[y][x-3] == 2: #4 
                score += 1000
                column_cord = y 
                row_cord = x
        if y == 0:
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2: #2
                score += 5
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2: #3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2 and copy_board[y+3][x] == 2: #4 
                score += 1000
                column_cord = y 
                row_cord = x
        
        if y == 1:
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2: #2
                score += 5
                column_cord = y 
                row_cord = x
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2: #3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2 and copy_board[y+3][x] == 2: #4 
                score += 1000
                column_cord = y 
                row_cord = x
            
        
        if y == 2:
            
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2: #2
                score += 5
                column_cord = y 
                row_cord = x
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2: #3
                score += 25 
                column_cord = y 
                row_cord = x
            
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2 and copy_board[y+3][x] == 2: #4 
                score += 1000
                column_cord = y 
                row_cord = x
            
        if y == 3:
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2: #2
                score += 5
                column_cord = y 
                row_cord = x
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2 and copy_board[y+2][x] == 2: #3
                score += 25 
                column_cord = y 
                row_cord = x
        if y == 4:
            if copy_board[y][x] == 2 and copy_board[y+1][x] == 2: #2
                score += 5
                column_cord = y 
                row_cord = x
        if y == 5:
            score += 0 
            column_cord = y 
            row_cord = x
            
            
            
            
            
            
            
            
            
         
            
            
       # for c in range(0,6): # 2 in a row (horizontal)
        #    if copy_board[y][c] == 2 and copy_board[y][c+1] == 2 :
         #       score +=25
          #      column_cord = y 
           #     row_cord = x
            #    break
        #for b in range(0,5): # 3 in a row (horizontal)
         #   if copy_board[y][b] == 2 and copy_board[y][b+1] == 2 and copy_board[y][b+2] == 2:
          #      score += 25
           #     column_cord = y 
            #    row_cord = x
             #   break
    
        #for a in range(0,4):# 4 in a row (horizontal)
         #   if copy_board[y][a] == 2 and copy_board[y][a+1] == 2 and copy_board[y][a+2] == 2  and copy_board[y][a+3] == 2:
          #      score += 50
           #     column_cord = y
            #    row_cord = x
             #   break
       
        #for f in range(0,5): # 2 in a row (verical)
         #   if copy_board[f][x] == 2 and copy_board[f+1][x] == 2:
          #      score += 25 
           #     column_cord = y 
            #    row_cord = x 
             #   break
        
       # for e in range(0,4): # 3 in a row (vertical)
        #    if copy_board[e][x] == 2 and copy_board[e+1][x] == 2 and copy_board[e+2][x] == 2:
         #       score += 25
          #      column_cord = y 
           #     row_cord = x 
            #    break
        
        #for d in range(0,3): # 4 in a row (vertical)
        #    if copy_board[d][x] == 2 and copy_board[d+1][x] == 2 and copy_board[d+2][x] == 2 and copy_board[d+3][x] == 2:
         #       score += 50
          #      column_cord = y 
           #     row_cord = x 
            #    break
        
        for g in range(3,6): # 4 in a row horizontal ne 
            for h in range(0,4):
                if copy_board[g][h] == 2 and copy_board[g-1][h+1] == 2 and copy_board[g-2][h+2] == 2 and copy_board[g-3][h+3] == 2:
                    score += 1000
                    column_cord = y 
                    row_cord = x 
                    break
       
        for i in range(3,6): # 3 in a row horizonal ne 
            for j in range(0,5):
                if copy_board[i][j] == 2 and copy_board[i-1][j+1] == 2 and copy_board[i-2][j+2] == 2:
                    score += 25 
                    column_cord = y 
                    row_cord = x 
                    break
        
        for k in range(3,6): # 2 in a row horizontal ne 
            for l in range(0,6):
                if copy_board[k][l] == 2 and copy_board[k-1][l+1] == 2:
                    score += 5 
                    column_cord = y 
                    row_cord = x 
                    break
        
        for m in range(3,6): # 4 in a row horizontal nw 
            for n in range(3,7):
                if copy_board[m][n] == 2 and copy_board[m-1][n-1] == 2 and copy_board[m-2][n-2] == 2 and copy_board[m-3][n-3] == 2:
                    score += 1000
                    column_cord = y 
                    row_cord = x 
                    break
        
        for m in range(3,6): # 3 in a row horizontal nw 
            for n in range(3,6):
                if copy_board[m][n] == 2 and copy_board[m-1][n-1] == 2 and copy_board[m-2][n-2] == 2:
                    score += 25
                    column_cord = y 
                    row_cord = x 
                    break
        
        for m in range(3,6): # 2 in a row horizontal nw 
            for n in range(3,5):
                if copy_board[m][n] == 2 and copy_board[m-1][n-1] == 2:
                    score += 5
                    column_cord = y 
                    row_cord = x 
                    break
        
        #print(score)
        copy_board[y][x] = 0 
        if copy_board[0][x] == 1 or copy_board[0][x] == 2:
            score = 0 
        bestmove.append(column_cord)
        bestmove.append(row_cord)
        bestmove.append(score)
        score = 0 
    
    return bestmove

def best_position(horizontal_ai):
    score_list=[]
    for i in horizontal_ai[2:21:3]:
        score_list.append(i)
    score=max(score_list)
    print("score:" , score)
    if score == 0:
        options = [0,1,2,3,4,5,6,]
        return random.choice(options)
    else:
        for a in range(0,7):
            if score_list[a] == score:
                pos_best= a + 1 
                break
            else:
                pass
        
        pos_best = pos_best * 3 
        pos_best = pos_best - 2
        return horizontal_ai[pos_best]

def terminal(gameboard):
    freespace = game_draw(gameboard)
    return win_condition_checker(gameboard) or freespace == 42
    
    
def minimax(gameboard, depth, maximizingplayer):
    freespace1 = freespace(gameboard)
    scoredmove = scoring_position(gameboard,freespace1) #returns a list of all the availble locations going [row] then [column] then the score for that position 
    #is terminal where the game is finished 4 in a row met returns true
    won = terminal(gameboard) 
    if depth == 0 or won:# won is true or false 
        if won:
            aiwin = ai_win(gameboard)
            playerwin = player_win(gameboard)
            if aiwin == 2:
                return 1000000000
            #if there is a 4 in a row for "2's" ai win therefore 
            #return a high positive integer
            if playerwin == 1:
                return -100000000
            else:
                return 0 
            #if there is a 4 in a row for 1's player win therefore
            #return a high negative integer
            #use gamedraw function (an else statement) if draw
            #returns 0 
            pass
        else: #depth is 0 
            
            
            #returns 
            pass
    
    if maximizingplayer:
        value = float('-inf')
        #for x in valid locations: # code for checking for all the columns which are not full and can input a result.
        for x,y in enumerate(freespace1):
            copyboard1 = copy.deepcopy(gameboard)
            copyboard1[y][x] = 2 
            score = max(value,minimax(copyboard1, depth-1, False))
            if score > value:
                value = score
        return value 
    
    else: # this is the minimizing player 
        value = float('inf')
        for x,y in enumerate(freespace1):
            copyboard1 = copy.deepcopy(gameboard)
            copyboard1[y][x] = 1 
            score = min(value,minimax(copyboard1, depth-1, True))
            if score < value:
                value = score
        return value
        
    

        
            
                
            
        pass
        
            
    
"-------------------------------------------------------------------"



"""Main Fuction The Gameloop"""        
def main():
    game_condition = False 
    row = 6 
    gameboard = board(row) # generates lists of 000000
    while not game_condition:
        
        player_input1 = user_input1(gameboard) # gets the user input 
        gameboard=board_updater1(player_input1,gameboard) #changing 0 to 1 
        game_condition = win_condition_checker(gameboard) #checks if player 1 won
        if game_condition:
            printboard(gameboard)
            break
        used_spaces = game_draw(gameboard) # checks for draw
        if used_spaces == 42:
            print("Game Draw")
            break
        #copy_board = copy.deepcopy(gameboard)
        #print(copy_board)
      
        
        
        freepsace = freespace(gameboard)
        aiscoring = scoring_position(gameboard,freepsace)
        #print(aiscoring)
        player_input2 = best_position(aiscoring)
        #print("column:" , player_input2)
        #player_input2 = user_input2(gameboard)
        gameboard = board_updater2(player_input2,gameboard)
        printboard(gameboard)
        game_condition = win_condition_checker(gameboard)
        used_spaces = game_draw(gameboard) 
        if used_spaces == 42:
            print("Game Draw")
            break
        
        
       
main()
