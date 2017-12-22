# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

def nome():
    nome = str(input('Qual seu nome? \n'))
    return nome
    
def simbolo():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Insira um símbolo válido.')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    return

def sorteio():
    j1 = nome
    j2 = computador
    sort = random.randint(1,2)
    if sort == 1:
        print ('Vencedor do sorteio para início do jogo: ' % j1)
    if sort == 2:
        print ('Vencedor do sorteio para início do jogo: ' % j2 )
    return





def mostrar_tabuleiro(tabuleiro) : 
    print((tabuleiro[0] [0])+'|'+(tabuleiro[0] [1])+'|'+(tabuleiro[0] [2]))
    print('')
    print((tabuleiro[1] [0])+'|'+(tabuleiro[1] [1])+'|'+(tabuleiro[1] [2]))
    print('')
    print((tabuleiro[2] [0])+'|'+(tabuleiro[2] [1])+'|'+(tabuleiro[2] [2]))
    return


v=[
    [1,1,1],
    [1,1,1],
    [1,1,1]]

def sorteios():
    sorteado = 1
    v.index(sorteado)
    print(v)
    
    
    
    
    
    
    
    
    
    
    
    
    