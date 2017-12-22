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

def jogadaHumano(nome, visual):
    jogada = input('Escolha sua jogada, %s' % nome)
    if not(visual[int(jogada[0])][int(jogada[2])] == ' ')
        print('Jogaga inválida')
        jogada = input('Escolha sua jogada, %s' % nome)
    return visual

def jogadaComputador(visual)
    jogada = ('%d %d' % (randint(0, 2), randint(0, 2)))
    if not(visual[int(jogada[0])][int(jogada[2])] == ' ')
        print('Jogaga inválida')
        jogada = input('Escolha sua jogada, %s' % nome)
    return visual
    
def montarVisual(visual):
    if i%2==0:
        visual[int(a[0])][int(a[2])]='X'
    else: 
        visual[int(a[0])][int(a[2])]='O'
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))

