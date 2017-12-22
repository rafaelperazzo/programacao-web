# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

def simbolo():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Isira um símbolo válido')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    return


def sorteio():
    j1 = 'nome'
    j2 = 'pc'
    sort = random.randint(1,2)
    if sort == 1:
        print ('Jogada da pessoa')
    else:
        print ('Jogada do pc')
    return

def mostrar_tabuleiro(tabuleiro) : 
    print((tabuleiro[0] [0])+'|'+(tabuleiro[0] [1])+'|'+(tabuleiro[0] [2]))
    print('')
    print((tabuleiro[1] [0])+'|'+(tabuleiro[1] [1])+'|'+(tabuleiro[1] [2]))
    print('')
    print((tabuleiro[2] [0])+'|'+(tabuleiro[2] [1])+'|'+(tabuleiro[2] [2]))
    return