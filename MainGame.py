#to do list:
#generate a scoring system for all 7 moves 
#which checks if its valid eg that column is full 
#.copy function to create new board to analyse 
#minimax algorithm to work(try on a diffrent file)
import random
import copy 
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
       
        if input2 ==1:
            column1 =[]
            for i in range(0,6):
                column1.append(gameboard[i][0])
            if 0 not in column1:
                print("Column 1 Full Select, Please Select Another Column")
            else:
                return input2
                break
            
        if input2 == 2:
            column2 = []
            for i in range(0,6):
                column2.append(gameboard[i][1])
            if 0 not in column2:
                print("Column 2 Full Select, Please Select Another Column")
                pass
            else:
                return input2
                break
            
        if input2 == 3:
            column3 = []
            for i in range(0,6):
                column3.append(gameboard[i][2])
            if 0 not in column3:
                print("Column 3 Full Select, Please Select Another Column")
                pass
            else:
                return input2
                break
            
        if input2 == 4:
            column4 = []
            for i in range(0,6):
                column4.append(gameboard[i][3])
            if 0 not in column4:
                print("Column 4 Full Select, Please Select Another Column")
                pass
            else:
                return input2
                break
            
        if input2 == 5:
            column5 = []
            for i in range(0,6):
                column5.append(gameboard[i][4])
            if 0 not in column5:
                print("Column 5 Full Select, Please Select Another Column")
                pass
            else:
                return input2
                break
            
        if input2 == 6:
            column6 = []
            for i in range(0,6):
                column6.append(gameboard[i][5])
            if 0 not in column6:
                print("Column 6 Full Select, Please Select Another Column")
                pass
            else:
                return input2
                break
        
        if input2 == 7:
            column7 = []
            for i in range(0,6):
                column7.append(gameboard[i][6])
            if 0 not in column7:
                print("Column 7 Full Select, Please Select Another Column")
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

def scoring_position(gameboard,freespace):
    copy_board = copy.deepcopy(gameboard)
    
    
    
    score = 0
    
    bestmove = []
    for x,y in enumerate(freespace):
        column_cord = 0
        row_cord = 0
        copy_board[y][x] = 2
        print(y,x) 
        for a in range(0,4):# 4 in a row (horizontal)
            if copy_board[y][a] == 2 and copy_board[y][a+1] == 2 and copy_board[y][a+2] == 2  and copy_board[y][a+3] == 2:
                score = 100 
                print(score)
                column_cord = y
                row_cord = x
                break
        for b in range(0,5): # 3 in a row (horizontal)
            if copy_board[y][b] == 2 and copy_board[y][b+1] == 2 and copy_board[y][b+2] == 2:
                if score == 100:
                    score = score 
                else:
                    score = 50 
                    column_cord = y 
                    row_cord = x
                break
        for c in range(0,6): # 2 in a row (horizontal)
            if copy_board[y][c] == 2 and copy_board[y][c+1] == 2 :
                if score == 100 or score == 50:
                    score = score
                else:
                    score=25
                    column_cord = y 
                    row_cord = x
                    break
        
        copy_board[y][x] = 0 
        bestmove.append(column_cord)
        bestmove.append(row_cord)
        bestmove.append(score)
        score = 0 
    
    return bestmove

def best_horizontal(horizontal_ai):
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

    
"-------------------------------------------------------------------"

def ai_input(gameboard):
    options = [1,2,3,4,5,6,7]
    return random.choice(options)

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
        horizontal_ai = scoring_position(gameboard,freepsace)
        player_input2 = best_horizontal(horizontal_ai)
        print("column:" , player_input2)
        #player_input2 = user_input2(gameboard)
        gameboard = board_updater2(player_input2,gameboard)
        printboard(gameboard)
        game_condition = win_condition_checker(gameboard)
        used_spaces = game_draw(gameboard) 
        if used_spaces == 42:
            print("Game Draw")
            break
        
        
       
main()
