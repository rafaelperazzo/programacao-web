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
    
def solicitaSimboloDoHumano():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Insira um símbolo válido.')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    if s == 'X':
        computador = 'O'
    else:
        computador = 'X'
    return

def sorteioPrimeiraJogada(nome):
    j1 = nome
    j2 = 'Computador'
    sort = random.randint(0,1)
    if sort == 1:
        return print ('Vencedor do sorteio para início do jogo: %s' % j1)
    if sort == 0:
        return print ('Vencedor do sorteio para início do jogo: %s' % j2)
    
def JogadaHumana(nome):
    c= int(input('Qual a sua jogada, %s? ' % nome))
    x = c // 10
    y = c % 10
    tabuleiro [x][y] = b
    return

#def validaJogada():
    
def validaJogada(tabuleiro) :
    linha = [0,1,2]
    coluna = [0,1,2]
    jogadapossivel = False
    # verifica se posicão escolhida é válida
    for r in linha :
        for c in coluna :
            k = str(r) + '-' + str(c)
            if not bool(board[key]) :
                return True
    return hasMoves





    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    