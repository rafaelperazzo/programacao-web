# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random
import os

#Simbolo que o Jogador quer utilizar
def solicitaSimbolodoHumano(a):
    a = input('\nQual símbolo você deseja utilizar no jogo? ')
    while a!='O' and a!='X' and a!='o' and a!='x':
        print('\nOPS!!! Esse símbolo não está disponível. Tente novamente!')
        a = input('\nQual símbolo você deseja utilizar no jogo? ')
    if a == 'x' or a == 'X':
        a = ' X '
    else:
        a = ' O '
    return a
    
    
    

#Sorteio de quem ira começar jogando
def sorteioPrimeiraJogada(jogador, nome):
    jogador = random.choice((0,1))
    if jogador == 1:
        print('\nVencedor do sorteio para inicio do jogo : %s'%nome)
        
    
    else:
        print('\nVencedor do sorteio para inicio do jogo : Computador')
        
    return jogador
    


#Printa o tabuleiro
def mostraTabuleiro(tabuleiro):
    print ('')
    print (tabuleiro[0][0] + '|' + tabuleiro[0][1] + '|' + tabuleiro[0][2])
    print (tabuleiro[1][0] + '|' + tabuleiro[1][1] + '|' + tabuleiro[1][2])
    print (tabuleiro[2][0] + '|' + tabuleiro[2][1] + '|' + tabuleiro[2][2])
    

#Jogada do computador  
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
    mostraTabuleiro(tabuleiro)
    return tabuleiro
    




#Verifica se a jogada é valida
def validaJogada(a, tabuleiro, nome):
    while True:
        ti = int(a[0])
        tj = int(a[2])
        if ti <3 and tj <3:
            if tabuleiro[int(a[0])][int(a[2])] == ('   '):
                break
            else:
                print('\nOPS!!! Essa jogada não está disponível. Tente novamente!')
                a = input('\nQual a sua jogada, %s? ' %nome)
        else:
            print('\nOPS!!! Essa jogada não está disponível. Tente novamente!')
            a = input('\nQual a sua jogada, %s? ' %nome)
    return a


#sua jogada
def JogadaHumana(smbH,tabuleiro, nome):
    
    n = input('\nQual a sua jogada, %s? ' %nome)
    n = validaJogada(n, tabuleiro, nome)
    tabuleiro[int(n[0])][int(n[2])] = smbH
    return tabuleiro
    







#Verifica se alguem ganhou
def verificaVencedor(simbolo, tabuleiro, som):
       
        if tabuleiro[0][0] == simbolo and tabuleiro[0][1] == simbolo and tabuleiro[0][2] == simbolo:
            return True

        elif tabuleiro[1][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[1][2] == simbolo:
            return True

        elif tabuleiro[2][0] == simbolo and tabuleiro[2][1] == simbolo and tabuleiro[2][2] == simbolo:
            return True

        elif tabuleiro[0][0] == simbolo and tabuleiro[1][0] == simbolo and tabuleiro[2][0] == simbolo:
            return True

        elif tabuleiro[0][1] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][1] == simbolo:
            return True
        
        elif tabuleiro[0][2] == simbolo and tabuleiro[1][2] == simbolo and tabuleiro[2][2] == simbolo:
            return True

        elif tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
            return True

        elif tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
            return True
        else:
            for i in range (0,3,1):
                for j in range (0,3,1):
                    if tabuleiro[i][j] == '   ':
                        som+=1
            if som == 0:
                som = 20
                return 20
            
        