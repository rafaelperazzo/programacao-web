# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def F1(x,y):
    return ((x*y)/(x-y))

def avaliar(z):
    resultado=z
    if z<0:
        resultado *= (-1)
    return resultado

def multiplicacao(x,y):

def funcao(a,b,c):
    if (a+b)==c:
        return True
    else:
        return False

def simbolo ():
    simbolo=str(input("Escolha um simbolo [X ou O]: "))
    while (simbolo!='X' and simbolo!='O'):
            print ("SIMBOLO INVALIDO!")
            simbolo=str(input("Escolha um simbolo [X ou O]: "))
    print ("pronto")
    

def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=i
    return f
    

def ler_inteiro():
    i=input(mensagem):
    return
    
    
def cronometro(s):
    for i in range(s,-1,-1):
        print ("%d segundos" %i)
        
def ler carta_baralho():
    while(True):
        carta= ler_inteiro("digite um numero")
        if (carta >=1 and carta <=13):
            break
        else:
            print ("CARTA INVALIDA")
    return carta
    """
