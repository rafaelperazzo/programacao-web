# -*- coding: utf-8 -*-
import random

tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
simbolos = ['X', 'O']
jogadasPossiveis = ['O','1','2']
def solicitaSimboloDoHumano():
    s = ''
    while True:
        s = input('\nQual símbolo você deseja utilizar no jogo? ')
        if not(s in simbolos):
            print('\nPor favor, selecione um símbolo válido: X ou O')
            continue
        if s == simbolo [0]
            return 0
        else:
             return 1
             
def sorteioPrimeiraJoagada(nome):
    r = random.randint(0,1)
    if r == 0:
        print('\nVencedor do sorteio para início do jogo: %s' % 'Computador')
    else:
        print('\nVencedor do sorteio para início do jogo: %s' % nome)
    return r
    
def validaJoagada(xy):
    if len(xy) != 2:
        return False
    if not xy[0] in joagadasPossiveis:
        return False
    if not xy[1] in joagadasPossiveis:
        return False
    x = int(xy[0])
    y = int(xy[1])
    
    if not tabuleiro[x][y] == ' ':
        return False
    return True
    
def jogadaHumana(nome, simboloIndex):
    while True:
        jogada = input('\nQual a sua joagada, %? '% nome)
        xy = jogada.split(' ')
        if validaJoagada(xy):
            x = int(xy[0])
            y = int(xy[1])
            tabuleiro[x][y] = simbolos[simboloIndex]
            break
        else:
            print('\nOPS!!! Essa joagada não está disponível. Tente novamente!')
            
    
            