# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
#def multiplicacao(x,y):
#    m= x * y
#   return m
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
    