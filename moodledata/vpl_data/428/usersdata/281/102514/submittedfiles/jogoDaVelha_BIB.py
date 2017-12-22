# -*- coding: utf-8 -*-
import random
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
jogo_da_velha=[]

def simb ():
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O? '))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O? '))

def sorteio (x,n):
    sorteio=random.choice((0,1))
    return(sorteio)
    

    
