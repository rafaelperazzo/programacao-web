# -*- coding: utf-8 -*-
import random

#Simbolo que o Jogador quer utilizar
def solicitaSimbolodoHumano(a):
    a = input('Simbolo que quer jogar: ')
    while a!='O' and a!='X' and a!='o' and a!='x':
        a = input('Simbolo que quer jogar: ')
    return 

#Sorteio de quem ira começar jogando
def sorteioPrimeiraJogada(a):
    a = random.choice((0,1))
    if a ==1:
        print('Vencedor do sorteio para inicio do jogo : Jogador')
    
    else:
        print('Vencedor do sorteio para inicio do jogo : Computador')
    return


#Jogada do computador
def jogadaComputador():
    a = random.choice(('0 0', '0 1','0 2','1 0', '1 1','1 2','2 0', '2 1','2 2'))
    tabuleiro[int(a[0])] [int(a[0])] = ' O '
    return 


#Verifica se alguem ganhou
def ganhou(simbolo, tabuleiro):
        if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
                return 1

        if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
                return 1

        if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
                return 1

        if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
                return 1
        
        if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
                return 1

        if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
                return 1


