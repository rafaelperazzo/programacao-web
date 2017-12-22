# -*- coding: utf-8 -*-
import random


def solicitaSimbolodoHumano(a):
    a = input('Simbolo que quer jogar: ')
    while a!='O' and a!='X' and a!='o' and a!='x':
        a = input('Simbolo que quer jogar: ')
    return 

def sorteioPrimeiraJogada(a):
    a = random.choice((0,1))
    if a ==1:
        print('Vencedor do sorteio para inicio do jogo : Jogador')
    
    else:
        print('Vencedor do sorteio para inicio do jogo : Computador')
    return

def jogadaComputador(a):
    a = random.choice(('0 0', '0 1','0 2','1 0', '1 1','1 2','2 0', '2 1','2 2'))
    tabuleiro[int(a[0])] [int(a[0])] = ' O '
    return 




