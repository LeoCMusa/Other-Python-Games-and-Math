import os

os.system('cls')

#|Variables and lists| -->
mats, final = [], []
ops = ["+", "-", "*", "det"]
op = ""



#|Define matrices| -->
num = int(input("number of matrices: "))
col = int(input("number of collums of the matrices(they must all be the same size): "))

for a in range(0, num):
    mat_ = []
    print(" ")
    print(f"insert {a + 1}º matrix(ex: 1 2 3)")
    print("                (    1 2 3)\n")
    for b in range(0, col):
        inter = input().split()
        for c in range(0, len(inter)):
            inter[c] = int(inter[c])
        mat_.append(inter)
    mats.append(mat_)



#|Define operation| -->
while(True):
    print(" ")
    op = input("operation(+,-,*,det): ")

    if op in ops:
        break

    else:
        print(" ")
        print("that is not a valid operation, try again")



#|Functions for operation: + and -| -->
def DoMaisOrMenos(mais):
    matrix = mats[0]
    for a in range(1, len(mats)):
        matrix = MaisAndMenos(matrix, mats[a], mais)
    return matrix

def MaisAndMenos(mat1, mat2, mais):
    mult = 0
    if mais:
        mult = 1
    else:
        mult = -1
    newMat = SetMatrizNull(len(mat2[0]), len(mat2))
    for a in range(0, len(mat2)):
        for b in range(0, len(mat2[0])):
            newMat[a][b] = mat1[a][b] + mult*mat2[a][b]
    return newMat



#|Functions for operation: *| -->
def DoVezes():
    matrix = mats[0]
    for a in range(1, len(mats)):
        matrix = Vezes(matrix, mats[a])
    return matrix

def Vezes(mat1, mat2):
    d = 0
    newMat = SetMatrizNull(len(mat2[0]), len(mat2))
    for a in range(0, len(mat2)):
        for b in range(0, len(mat2[0])):
            for c in range(0, len(mat2)):
                d += mat1[a][c]*mat2[c][b]
            newMat[a][b] = d
            d = 0
    return newMat



#|FUnctions for operation: det| -->
def PrintDets(mat):
    for a in range(0, len(mat)):
        print(f"{a+1}ª {mat[a]}")
    
def DoDet():
    matDet = []
    for a in range(0, len(mats)):
        matDet.append(Determinante(mats[a]))
    return matDet

def Determinante(mat):
    hight = len(mat)
    det = 0
    if hight == 3:
        det = DetMin(mat, 3)
    elif hight == 2:
        det = DetMin(mat, 2)
    else:
        for a in range(0, hight):
            det += mat[a][0]*Cof(mat, a, 0)
            
    return det

def DetMin(mat, tam):
    det = 0
    if tam == 2:
        det = mat[0][0]*mat[1][1] + mat[0][1]*mat[1][0] - mat[0][1]*mat[1][0] - mat[0][0]*mat[1][1]
    elif tam == 3:
        det = mat[0][0]*mat[1][1]*mat[2][2] + mat[0][1]*mat[1][2]*mat[2][0] + mat[0][2]*mat[1][0]*mat[2][1] - mat[0][2]*mat[1][1]*mat[2][0] - mat[0][0]*mat[1][2]*mat[2][1] - mat[0][1]*mat[1][0]*mat[2][2] 

    return det

def Cof(mat, inda, indb):
    cof = 0
    newMat = []
    inter = []
    for a in range(0, len(mat)):
        inter = []
        if a != inda:
            for b in range(1, len(mat[0])):
                inter.append(mat[a][b])
            newMat.append(inter)
    return Determinante(newMat)*((-1)**(inda+indb+2))


#|Miscellaneous| -->
def NumOp(mats):
    a = len(mats)
    if len(mats)%2 != 0:
        a += 0,5
    return a

def PrintMatriz(matriz):
    for a in range(0, len(matriz)):
        print(matriz[a])

def SetMatrizNull(length, hight):
    matriz = []
    matrizfinal = []
    for a in range(0, length):
        for b in range(0, hight):
            matriz.append(0)
        matrizfinal.append(matriz)
        matriz = []
            
    return matrizfinal



#|MAIN| -->
def Main():

    if op == "+":
        final = DoMaisOrMenos(True)
        os.system('cls')
        print("The sum of those matrices is: ")
        PrintMatriz(final)

    elif op == "_":
        final = DoMaisOrMenos(False)
        os.system('cls')
        print("The subtraction of those matrices is: ")
        PrintMatriz(final)

    elif op == "*":
        final = DoVezes()
        os.system('cls')
        print("The multiplication of those matrices is: ")
        PrintMatriz(final)
    
    elif op == "det":
        final = DoDet()
        os.system('cls')
        print("The determinants of the matrix(s) are: ")
        PrintDets(final)

Main()
