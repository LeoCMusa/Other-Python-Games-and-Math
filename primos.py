#testendo se o número ao quadrado menos 1 é divisível por 24 ou não
def divisor(num):
    
    vinte_quatro = False
    if num > 1:

        if((num**2)-1) >= 24:
            if((num**2)-1)%24 == 0:
                vinte_quatro = True

        if((num**2)-1) < 24:
            if 24%((num**2)-1) == 0:
                vinte_quatro = True

    if vinte_quatro == True:
        return(True)
    else:
        return(False)

#achando os números primos
def PrimeFinder(lista, maximo):

    boole = False

    for a in range(1, maximo):
        if divisor(a):
                for b in range(2, int((a**(1/2)+2))):
                    if a == b:
                        boole = True
                        break
                    if a%b == 0:
                        boole = False
                        break
                    else:
                        boole = True
                #coloca em uma lista
                if boole == True:
                    lista.append(a)

