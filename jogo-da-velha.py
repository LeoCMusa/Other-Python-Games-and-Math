roll1 = ["  ", "  ", "  "]
roll2 = ["  ", "  ", "  "]
roll3 = ["  ", "  ", "  "]
roll = [roll1, roll2, roll3]

def tabela():
    print("{} | {} | {}".format(roll1[0], roll1[1], roll1[2]))
    print("——   ——   ——")
    print("{} | {} | {}".format(roll2[0], roll2[1], roll2[2]))
    print("——   ——   ——")
    print("{} | {} | {}".format(roll3[0], roll3[1], roll3[2]))

def casos():
    if roll[0][0] == roll[0][1] and roll[0][0] == roll[0][2] and roll[0][0] != "  ":
        return True
    elif roll[1][0] == roll[1][1] and roll[1][0] == roll[1][2] and roll[1][0] != "  ":
        return True
    elif roll[2][0] == roll[2][1] and roll[2][0] == roll[2][2] and roll[2][0] != "  ":
        return True
    elif roll[0][0] == roll[1][0] and roll[0][0] == roll[2][0] and roll[0][0] != "  ":
        return True
    elif roll[0][1] == roll[1][1] and roll[0][1] == roll[2][1] and roll[0][1] != "  ":
        return True
    elif roll[0][2] == roll[1][2] and roll[0][2] == roll[2][2] and roll[0][2] != "  ":
        return True
    elif roll[0][0] == roll[1][1] and roll[0][0] == roll[2][2] and roll[0][0] != "  ":
        return True
    elif roll[0][2] == roll[1][1] and roll[0][2] == roll[2][0] and roll[0][2] != "  ":
        return True

def jogo():
    while True:
        a = input("Jogador1: ")
        roll[int(a[0])][int(a[1])] = "x "
        tabela()
        if casos():
            print("vitória de jogador 1!")
            print("")
            break

        b = input("Jogador2: ")
        roll[int(b[0])][int(b[1])] = "O "
        tabela()
        if casos():
            print("vitória de jogador 2!")
            print("recomeçando...")
            print("")
            break

def main():
    while True:
        inicio = input("Quer começar um novo jogo?(s/n)")
        if inicio == "s":
            print("")
            print("Você iniciou um novo jogo da velha!")
            print("O jogador 1 será 'x' e o jogador 2 será 'O'")
            print("Para escolher sua posição digite primeiro a fileira(de 0 a 2) e logo após a coluna(de 0 a 2)")
            print("")
            jogo()
            roll1 = ["  ", "  ", "  "]
            roll2 = ["  ", "  ", "  "]
            roll3 = ["  ", "  ", "  "]
            roll = [roll1, roll2, roll3]
        elif inicio == "n":
            break
        else:
            print("isso não é uma resposta válida")

main()