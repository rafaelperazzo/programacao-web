# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

tabuleiro =[
    [1,1,1],
    [1,1,1],
    [1,1,1]]

def nome():
    nome = str(input('Qual seu nome? \n'))
    return nome
    
def simbolo():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Insira um símbolo válido.')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    if s == 'X':
        computador = 'O'
    else:
        computador = 'X'
    return

def sorteio(nome):
    j1 = nome
    j2 = 'Computador'
    sort = random.randint(0,1)
    if sort == 1:
        return print ('Vencedor do sorteio para início do jogo: %s' % j1)
    if sort == 0:
        return print ('Vencedor do sorteio para início do jogo: %s' % j2)
    
def JogadaHumano(nome):
    c= int(input('Qual a sua jogada, %s? ' % nome))
    x = c // 10
    y = c % 10
    tabuleiro [x][y] = s
    return




    
'''def jogada_pc():
    j1 =
    j2 = 
    sort = random.randint(0,1)
    if sort == 1:
        return
    if sort == 0:
        return'''





def mostrar_tabuleiro(tabuleiro) : 
    print((tabuleiro[0] [0])+'|'+(tabuleiro[0] [1])+'|'+(tabuleiro[0] [2]))
    print('')
    print((tabuleiro[1] [0])+'|'+(tabuleiro[1] [1])+'|'+(tabuleiro[1] [2]))
    print('')
    print((tabuleiro[2] [0])+'|'+(tabuleiro[2] [1])+'|'+(tabuleiro[2] [2]))
    return




def jogada():
    sorteado = 1
    print(v.index(sorteado))
    v.remove(sorteado)
    
    
    
    
    
    
    
    
    
    
    
    
    
    