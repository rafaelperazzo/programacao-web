# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def maximo (a,b):
    if a>b:
        return a
    else:
        return b
    
lista1.append(input('Digite um valor: '))
lista1[len(lista1)]
len(lista1)
lista1[len(lista1)-1]
lista1[len(lista1)+1]


def par(n):
    if (n%2)==0:
        return True
    else:
        return False

def f1(x,y):
    return ((x*y)/(x-y))

def avaliar(z):
    resultado=z
    if z<0:
        resultado *= (-1)
    return resultado

def multiplicacao(x,y):
    return (x*y)

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
    i=input('mensagem: ')
    return i
    
    
def cronometro(s):
    for i in range(s,-1,-1):
        print ("%d segundos" %i)
        
