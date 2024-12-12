import matplotlib.pyplot as plt
import numpy as np

N = []
matriz = []
I = []
tamanho = 100
pontos = 100000
tamanhoTotal = np.linspace(-tamanho, tamanho, pontos)


def Main():
    #definindo inputs
    grau = int(input("Grau da função: "))
    for a in range(0, grau+1):
        N.append(float(input("coeficiente {}: ".format(a+1))))
    
    #cria Lista de y para todo x dentro do tamanho(Imagem)
    I = ListFunc()

    #criando o gráfico
    fig, ax = plt.subplots()
    plt.plot(tamanhoTotal, I)
    ax.grid(True, 'major', linestyle='-')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title("função de grau{}".format(grau))
    if grau == 2: 
         ax.annotate("Vértice({}, {})".format(Vertice(N)[0], Vertice(N)[1]), (Vertice(N)[0], Vertice(N)[1]))
    plt.show()

#funcão que é literalmente a função (pega um x e cria y)
def Função(x):
    y = 0
    for b in range(0, len(N)):
        y += N[b] * x**(len(N)-b-1)
    return(y)

def ListFunc():
    lista = []
    for i in tamanhoTotal:
            lista.append(Função(i))
    return(lista)

#função para achar o vértice da função de 2º grau
def Vertice(N):
    x = (-N[1])/(2*N[0])
    delta = N[1]**2 - 4*N[0]*N[2]
    y = -delta / (4*N[0])
    ver = (x, y)
    return(ver)
    
Main()
