# -*- coding: utf-8 -*-
from random import randint
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def solicitaNomeDoJogador():
    nome=str(input('Qual o seu nome ou (apelido)? '))
    return nome
    
def solicitaSimboloDoHumano():
    simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    while simbolo not in ('X','O'):
        simbolo=str.upper(input('Qual simbolo você deseja utilizar no jogo? '))
    if simbolo== 'X':
        scomputador='O'
    else:
        scomputador='X'
    return [simbolo, scomputador]

def sorteioPrimeiraJogada(nomes):
    resultado = randint(0, 1)
    print('Vencedor do sorteio: %s' % nomes[resultado][0])
    return resultado

def jogadaHumano(nome, visual):
    jogada = input('Escolha sua jogada, %s: ' % nome[0])
    while not(visual[int(jogada[0])][int(jogada[2])] == ' '):
        print('Jogada inválida')
        jogada = input('Escolha sua jogada, %s: ' % nome[0])
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual

def jogadaComputador(nome, visual):
    jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    while not(visual[int(jogada[0])][int(jogada[2])] == ' '):
        jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    visual[int(jogada[0])][int(jogada[2])] = nome[1]
    return visual
    
def mostraTabuleiro(i, visual):
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))

