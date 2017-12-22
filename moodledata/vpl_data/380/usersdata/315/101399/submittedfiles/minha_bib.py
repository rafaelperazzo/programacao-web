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
        if tabuleiro[0][0] == simbolo and tabuleiro[0][1] == simbolo and tabuleiro[0][2] == simbolo:
                return True

        if tabuleiro[1][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[1][2] == simbolo:
                return True

        if tabuleiro[2][0] == simbolo and tabuleiro[2][1] == simbolo and tabuleiro[2][2] == simbolo:
                return True

        if tabuleiro[0][0] == simbolo and tabuleiro[0][1] == simbolo and tabuleiro[0][2] == simbolo:
                return True

        if tabuleiro[1][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[1][2] == simbolo:
                return True
        
        if tabuleiro[2][0] == simbolo and tabuleiro[2][1] == simbolo and tabuleiro[2][2] == simbolo:
                return True

        if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
                return True

        if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
                return True


