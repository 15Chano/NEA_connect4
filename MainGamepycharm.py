#import random 
#f strings 

def board(row):
    board1=[]
    for i in range(0,row):
        board1.append([0,0,0,0,0,0,0])
    return board1
    #print(board[5]) # 6 lists but when put in [], [0] counts as the first list 
    #print(board[1][2]) # adding another [] here can output which place of the second list

    
def check_win_vertical():
    pass
    
def user_input(gameboard):
    def player1input():
        Player1 = int(input("Player One Input Column Number 1-6:"))
        return Player1
    Player1 = player1input()
    if Player1 < 1 or Player1> 6:
        print("Try Again, Numbers Can Only Be 1,2,3,4,5,6")
        player1input()
    else:
        if gameboard[5][Player1-1] == 0:
            gameboard[5][Player1-1] = 1
            
def gameloop(gameboard):
    def printboard():
        print(gameboard[0])
        print(gameboard[1])
        print(gameboard[2])
        print(gameboard[3])
        print(gameboard[4])
        print(gameboard[5])
           
def main():
    row = 6 
    gameboard = board(row)
    user_input(gameboard)
    
  

main()
    
 
