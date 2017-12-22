# -*- coding: utf-8 -*-
import random

#Simbolo que o Jogador quer utilizar
def solicitaSimbolodoHumano(a):
    a = input('Simbolo que quer jogar: ')
    while a!='O' and a!='X' and a!='o' and a!='x':
        a = input('Simbolo que quer jogar: ')
    if a == 'x' or a =='X':
        a = ' X '
    else:
        a = ' O '
    return a

#Sorteio de quem ira começar jogando
def sorteioPrimeiraJogada(jogador):
    jogador = random.choice((0,1))
    if jogador ==1:
        print('Vencedor do sorteio para inicio do jogo : Jogador')
        
    
    else:
        print('Vencedor do sorteio para inicio do jogo : Computador')
        
    return jogador


#Jogada do computador   TA COM ERRO
def JogadaComputador(smbPC,tabuleiro):
    
    while True:
        ti = random.choice((0,1,2))
        tj = random.choice((0,1,2))
        if tabuleiro[ti][tj] == '   ':
            break
        else:
            ti = random.choice((0,1,2))
            tj = random.choice((0,1,2))
    tabuleiro[ti][tj] = smbPC
    return tabuleiro
    



def validaJogada(a):
    a = input('Qual a sua jogada, %s' %nome)
    while True:
        if tabuleiro[int(a[0])][int(a[2])] == '   ':
            break
        else:
            print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            a = input('Qual a sua jogada, %s' %nome)
        return a

def JogadaHumana(smbH,tabuleiro):
    print (tabuleiro[0][0] + '|' + tabuleiro[0][1] + '|' + tabuleiro[0][2])
    print (tabuleiro[1][0] + '|' + tabuleiro[1][1] + '|' + tabuleiro[1][2])
    print (tabuleiro[2][0] + '|' + tabuleiro[2][1] + '|' + tabuleiro[2][2])
    validaJogada(n)
    tabuleiro[int(n[0])][int(n[2])] = smbH
    return tabuleiro
    







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


