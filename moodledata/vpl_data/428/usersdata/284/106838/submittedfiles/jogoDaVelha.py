# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI

#definir entrada em lista:

import random

def solicitaSimboloDoHumano():
    letra = 0
    while not (letra == 'O' or letra == 'X'):
        print('Qual símbolo você deseja utilizar no jogo? (X ou O) ')
        letra = input().upper()

    if letra == 'X':
        return ['X','O']
    else:
        return ['O','X']

def sorteioPrimeiraJogada():
    if random.randint(1,2) == 1:
        return 'Computador'
    else:
        return 'Jogador'
#movimento em forma de vetor/matriz:

def jogadaHumana(tabuleiro):
    movimento = 0
    while movimento not in '1 2 3 4 5 6 7 8 9'.split() or not vazio(tabuleiro, int(movimento)):
        print('Qual a sua jogada, {}?'.format(nome))
        movimento = input()
        if movimento == 7:
            movimento = 0_0
            if movimento == 8:
                movimento = ('0 1')
                if movimento == 9:
                    movimento = ('0 2')
                    if movimento == 4:
                        movimento = ('1 0')
                        if movimento == 5:
                            movimento = ('1 1')
                            if movimento == 6:
                                movimento = ('1 2')
                                if movimento == 1:
                                    movimento = ('2 0')
                                    if movimento == 2:
                                        movimento = ('2 1')
                                        if movimento == 3:
                                            movimento = ('2 2')
    return int(movimento)
#função com relação a matrizes:

def jogadaComputador(tabuleiro, letraComputador):
    if letraComputador == 'X':
        letraJogador = 'O'
    else:
        letraJogador = 'X'
    for i in range(1,10):
        copy = mostraTabuleiro(tabuleiro)
        if vazio(copy, i):
            movimentacao(copy, letraComputador, i)
            if verificaVencedor(copy, letraComputador):
                return i

    for i in range(1, 10):
        copy = mostraTabuleiro(tabuleiro)
        if vazio(copy, i):
            movimentacao(copy, letraJogador, i)
            if verificaVencedor(copy, letraJogador):
                return i

    movimento = movAleatoria(tabuleiro, [1, 3, 7, 9])
    if movimento != None:
        return movimento

    if vazio(tabuleiro, 5):
        return 5

    return movAleatoria(tabuleiro, [2, 4, 6, 8])

#def validaJogada()

def mostraTabuleiro(tabuleiro):
    dupeTabuleiro = []

    for i in tabuleiro:
        dupeTabuleiro.append(i)

    return dupeTabuleiro

def verificaVencedor(tabuleiro, letra):
    return ((tabuleiro[7] == letra and tabuleiro[8] == letra and tabuleiro[9] == letra) or
    (tabuleiro[4] == letra and tabuleiro[5] == letra and tabuleiro[6] == letra) or
    (tabuleiro[1] == letra and tabuleiro[2] == letra and tabuleiro[3] == letra) or
    (tabuleiro[7] == letra and tabuleiro[4] == letra and tabuleiro[1] == letra) or
    (tabuleiro[8] == letra and tabuleiro[5] == letra and tabuleiro[2] == letra) or
    (tabuleiro[9] == letra and tabuleiro[6] == letra and tabuleiro[3] == letra) or
    (tabuleiro[7] == letra and tabuleiro[5] == letra and tabuleiro[3] == letra) or
    (tabuleiro[9] == letra and tabuleiro[5] == letra and tabuleiro[1] == letra))

#################################################################################
def vazio(tabuleiro, movimento):
    return tabuleiro[movimento] == ' '

def desenhaTabuleiro(tabuleiro):
    print(' ' + tabuleiro[7] + ' | ' + tabuleiro[8] + ' | ' + tabuleiro[9])
    print(' ' + tabuleiro[4] + ' | ' + tabuleiro[5] + ' | ' + tabuleiro[6])
    print(' ' + tabuleiro[1] + ' | ' + tabuleiro[2] + ' | ' + tabuleiro[3])



def jogarNovamente():
    print('Você deseja jogar novamente?(sim ou não)')
    return input().lower().startswith('sim')

def movimentacao(tabuleiro, letra, movimento):
    tabuleiro[movimento] = letra





def movAleatoria(tabuleiro, movimentosList):
    movPossiveis = []
    for i in movimentosList:
        if vazio(tabuleiro, i):
            movPossiveis.append(i)

    if len(movPossiveis) != 0:
        return random.choice(movPossiveis)
    else:
        return None

    

def completo(tabuleiro):
    for i in range(1, 10):
        if vazio(tabuleiro, i):
            return False
    return True


print('Bem vindo ao JogoDaVelha do grupo X')
nome = input('Qual o seu nome (ou apelido)? ')
while True:
    tabul = [' '] * 10
    letraJogador, letraComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print('Vencedor do sorteio para início do jogo: {}'.format(turn))
    rodando = True

    while rodando:
        if turn == 'Jogador':
            desenhaTabuleiro(tabul)
            movimento = jogadaHumana(tabul)
            movimentacao(tabul, letraJogador, movimento)

            if verificaVencedor(tabul, letraJogador):
                desenhaTabuleiro(tabul)
                print('Vencedor: {}'.format(nome))
                rodando = False
            else:
                if completo(tabul):
                    desenhaTabuleiro(tabul)
                    print('Deu Velha!')
                    break
                else:
                    turn = 'Computador'

        else:
            movimento = jogadaComputador(tabul, letraComputador)
            movimentacao(tabul, letraComputador, movimento)

            if verificaVencedor(tabul, letraComputador):
                desenhaTabuleiro(tabul)
                print('Vencedor: Computador')
                rodando = False
            else:
                if completo(tabul):
                    desenhaTabuleiro(tabul)
                    print('Deu Velha!')
                    break
                else:
                    turn = 'Jogador'

    if not jogarNovamente():
        break
