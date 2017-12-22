# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
import random 
def solicitaSimboloDoHumano():
    simbolo=str(input("Escolha um simbolo para jogar (X,O): "))
    while (simbolo)!= 'X' and (simbolo)!='O':
        print ("Simbolo invalido,seu burro!")
        simbolo=str(input("Escolha um simbolo certo para jogar! (X,O): "))
    if simbolo=='X':
        return ['X','O']
    else:
        return ['O','X']

def sorteioPrimeiraJogada():
    if random.randint(1,2)==1:
        return 'Computador'
    else:
        return 'Voce'

#movimento em forma de vetor/matriz:

def jogadaHumana(tabuleiro):
    movimento = 0
    while movimento not in '1 2 3 4 5 6 7 8 9'.split() or not vazio(tabuleiro, int(movimento)):
        print('Qual a sua jogada, {}?'.format(nome))
        movimento = input()
    return int(movimento)
#função com relação a matrizes:

def jogadaComputador(tabuleiro, simboloComputador):
    if simboloComputador == 'X':
        simboloVoce = 'O'
    else:
        simboloVoce = 'X'
    for i in range(1,10):
        copy = mostraTabuleiro(tabuleiro)
        if vazio(copy, i):
            movimentacao(copy, simboloComputador, i)
            if verificaVencedor(copy, simboloComputador):
                return i

    for i in range(1, 10):
        copy = mostraTabuleiro(tabuleiro)
        if vazio(copy, i):
            movimentacao(copy, simboloVoce, i)
            if verificaVencedor(copy, simboloVoce):
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

def verificaVencedor(tabuleiro, simbolo):
    return ((tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo) or  #linhas vencedoras
 (tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] ==simbolo) or     
 (tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo) or
 (tabuleiro[7] == simbolo and tabuleiro[4] == simbolo and tabuleiro[1] == simbolo) or              #colunas vencedoras
 (tabuleiro[8] == simbolo and tabuleiro[5] == simbolo and tabuleiro[2] == simbolo) or     
 (tabuleiro[9] == simbolo and tabuleiro[6] == simbolo and tabuleiro[3] == simbolo) or  
 (tabuleiro[7] == simbolo and tabuleiro[5] == simbolo and tabuleiro[3] == simbolo) or      #diagonais vencedoras
 (tabuleiro[9] == simbolo and tabuleiro[5] == simbolo and tabuleiro[1] == simbolo))
 

#################################################################################
def vazio(tabuleiro, movimento):
    return tabuleiro[movimento] == ' '

def desenhaTabuleiro(tabuleiro):
    print(' ' + tabuleiro[7] + ' | ' + tabuleiro[8] + ' | ' + tabuleiro[9])
    print(' ' + tabuleiro[4] + ' | ' + tabuleiro[5] + ' | ' + tabuleiro[6])
    print(' ' + tabuleiro[1] + ' | ' + tabuleiro[2] + ' | ' + tabuleiro[3])



def jogarNovamente():
    jogar=str(input('Você deseja jogar novamente? '))
    if jogar==("SIM"):
        return True
    elif jogar==("NAO"):
        return False

def movimentacao(tabuleiro, simbolo, movimento):
    tabuleiro[movimento] = simbolo





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


print('Bem vindo ao Jogo Da Velha do ultimo grupo')
nome = input('Qual o seu nome? ')
while True:
    tabul = [' '] * 10
    simboloVoce, simboloComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print ("\n")
    print ("\nPosições jogáveis")
    print ("\n 7 | 8 | 9 ")
    print ("---+---+---")
    print (" 4 | 5 | 6 ")
    print ("---+---+---") 
    print (" 1 | 2 | 3 ")
    print ("\n")  
    print ("______________________________________________")
    print ("\n Começou!")
    print("\nVencedor do sorteio para início do jogo: {}".format(turn))
    print ("\n")
    rodando = True

    while rodando:
        if turn == 'Voce':
            desenhaTabuleiro(tabul)
            movimento = jogadaHumana(tabul)
            movimentacao(tabul, simboloVoce, movimento)

            if verificaVencedor(tabul, simboloVoce):
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
            movimento = jogadaComputador(tabul, simboloComputador)
            movimentacao(tabul, simboloComputador, movimento)

            if verificaVencedor(tabul, simboloComputador):
                desenhaTabuleiro(tabul)
                print('Vencedor: Computador')
                rodando = False
            else:
                if completo(tabul):
                    desenhaTabuleiro(tabul)
                    print('Deu Velha!')
                    break
                else:
                    turn = 'Voce'

    if jogarNovamente():
        continue
    else:
        break
print ("Ate mais!")
