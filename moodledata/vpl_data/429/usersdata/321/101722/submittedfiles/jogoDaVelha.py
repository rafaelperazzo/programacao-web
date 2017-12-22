# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')
nome = str(input('Qual seu nome? \n'))

simbolo()

sorteio()

tabuleiro = [
    ['','',''],
    ['','',''],
    ['','','']]
    
def printCell(cell) :
    if cell : 
        return ' '+str(cell)+' '
    else :
        return '   '
    
def showBoard(board) : 
    print(printCell(tabuleiro[0] [0])+'|'+printCell(tabuleiro[0] [1])+'|'+printCell(tabuleiro[0] [2])
    print('')
    print(printCell(tabuleiro[1] [0]])+'|'+printCell(tabuleiro[1] [1])+'|'+printCell(tabuleiro[1] [2]))
    print('')
    print(printCell(tabuleiro[2] [0])+'|'+printCell(tabuleiro[2] [1])+'|'+printCell(tabuleiro[2] [2]))