def GetBoard(board):
    print(" " + "0" + " " + "1" + " " + "2" + " " + "3" + " " + "4" + " " + "5" + " " + "6")
    print("|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|" + board[0][3] + "|" + board[0][4] + "|" + board[0][5] + "|" + board[0][6] + "|")
    print("|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" + board[1][3] + "|" + board[1][4] + "|" + board[1][5] + "|" + board[1][6] + "|")
    print("|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" + board[2][3] + "|" + board[2][4] + "|" + board[2][5] + "|" + board[2][6] + "|")
    print("|" + board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" + board[3][3] + "|" + board[3][4] + "|" + board[3][5] + "|" + board[3][6] + "|")
    print("|" + board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" + board[4][3] + "|" + board[4][4] + "|" + board[4][5] + "|" + board[4][6] + "|")
    print("|" + board[5][0] + "|" + board[5][1] + "|" + board[5][2] + "|" + board[5][3] + "|" + board[5][4] + "|" + board[5][5] + "|" + board[5][6] + "|")
    print("|" + board[6][0] + "|" + board[6][1] + "|" + board[6][2] + "|" + board[6][3] + "|" + board[6][4] + "|" + board[6][5] + "|" + board[6][6] + "|")

def Wins(b, win):
    countX = 0
    countO = 0
    if win == " ":
        for c in range(0, 7):
            if win == " ":
                for d in range(0,7):
                    
                    if win == " ":
                        countX = 0
                        countO = 0
                        for e in range(0,4):
                            if d + e <= 6:
                                if b[c][d + e] == "X":
                                   countX += 1
                                if b[c][d + e] == "O":
                                   countO += 1
                        if countX == 4:
                            win = "X"
                        if countO == 4:
                            win = "O"

                    if win == " ":
                        countX = 0
                        countO = 0
                        for e in range(0,4):
                            if c + e <= 6:
                                if b[c + e][d] == "X":
                                   countX += 1
                                if b[c + e][d] == "O":
                                   countO += 1
                        if countX == 4:
                            win = "X"
                        if countO == 4:
                            win = "O"
                  
                    if win == " ":
                        countX = 0
                        countO = 0
                        for e in range(0,4):
                            if c + e <= 6 and d + e <= 6:
                                if b[c + e][d + e] == "X":
                                   countX += 1
                                if b[c + e][d + e] == "O":
                                   countO += 1
                        if countX == 4:
                            win = "X"
                        if countO == 4:
                            win = "O"

                    if win == " ":
                        countX = 0
                        countO = 0
                        for e in range(0,4):
                            if c - e >= 0 and d + e <= 6:
                                if b[c - e][d + e] == "X":
                                   countX += 1
                                if b[c - e][d + e] == "O":
                                   countO += 1
                        if countX == 4:
                            win = "X"
                        if countO == 4:
                            win = "O"

    return(win)

def Game(board, cel, win):
            GetBoard(board)
            while True:
                O = int(input("Jogador número 1! Insira o número da coluna na qual deseja colocar a sua peça(0 a 6): "))
                cel = 0
                for a in range(0, 7):
                    if board[a][O] == " ":
                        cel = a
                board[cel][O] = "O"
                GetBoard(board)
                win = " "
                win = Wins(board, win)
                if win == "O":
                    print("jogador1 venceu!")
                    break
                X = int(input("Jogador número 2! Insira o número da coluna na qual deseja colocar a sua peça(0 a 6): "))
                cel = 0
                for b in range(0, 7):
                    if board[b][X] == " ":
                        cel = b
                board[cel][X] = "X"
                GetBoard(board)
                win = " "
                win = Wins(board, win)
                if win == "X":
                    print("jogador2 venceu!")
                    break
                    
def Main():              
    while True:
        roll0 = [" ", " ", " ", " ", " ", " ", " "]
        roll1 = [" ", " ", " ", " ", " ", " ", " "]
        roll2 = [" ", " ", " ", " ", " ", " ", " "]
        roll3 = [" ", " ", " ", " ", " ", " ", " "]
        roll4 = [" ", " ", " ", " ", " ", " ", " "]
        roll5 = [" ", " ", " ", " ", " ", " ", " "]
        roll6 = [" ", " ", " ", " ", " ", " ", " "]
        board =[roll0, roll1, roll2, roll3, roll4, roll5, roll6]
        cel = 0
        win = " "
        if input("Bem-Vindo à Lig4, quer começar uma nova rodada? s/n: ") == "s":
             Game(board, cel, win)
        else:
            break

Main()
        
