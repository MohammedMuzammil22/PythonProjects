def displayBoard():
    for i in range(3):
            print(board[i][0],"|",board[i][1],"|",board[i][2])
            if(i!=2):
                print("--+---+--")
            
def win(board):
    for i in range(1):
        # row
        for i in range(3):
            if(board[i][0]==board[i][1]==board[i][2] and board[i][2]!=" "):
                return 1
        
        # col
        for i in range(3):
            if(board[0][i]==board[1][i]==board[2][i] and board[2][i]!=" "):
                return 1
                
        # diag
        if(board[0][0]==board[1][1]==board[2][2] and board[2][2]!=" "):
            return 1
        elif(board[2][0]==board[1][1]==board[0][2] and board[0][2]!=" "):
            return 1

def draw(board):
    if(" " not in board):
        return 1

def position(board,z):
    x = int(input("select position from 1-9 :"))
    while(x<0 or x>9):
        x = int(input("select position from 1-9 :"))
    y = x-1
    flag = 1
    for i in range(3):
        if (flag == 1):
            for j in range(3):
                if y !=0:
                    y -= 1
                else:
                    if(board[i][j]!= " "):
                        print("Pos '",x,"' already selected, select another pos")
                        return -11
                        
                    board[i][j]=z
                    flag = -1
                    break

def player1():
    x = "X"
    if(position(board,x)==-11):
        position(board,x)

def player2():
    o = "O"
    if(position(board,o)==-11):
        position(board,o)

play=""
while(play.lower()!="no"):
    board = [[" " for i in range(3)]for i in range(3)]
    start = 5
    while(start != 0):
        displayBoard()
        player1()
        w = win(board)
        if w==1:
            displayBoard()
            print("Player 'X' have won the game")
            break
        displayBoard()
        if(start==1):
            draw(board)
            print("The game is draw")
            break
        player2()
        w = win(board)
        if w==1:
            displayBoard()
            print("Player 'O' have won the game")
            break
        start -= 1
    play = input("do you want to play again (yes/no): ")