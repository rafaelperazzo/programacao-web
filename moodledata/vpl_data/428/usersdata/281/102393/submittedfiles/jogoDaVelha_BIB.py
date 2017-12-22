# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

def simb ():
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O?'))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O?'))

def sorteio ():
    sorteio=random.choice((1,0))

def mostratabuleiro(board):
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])
        


    



    
        