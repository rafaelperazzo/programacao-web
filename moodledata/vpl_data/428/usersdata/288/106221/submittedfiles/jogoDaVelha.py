# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
import random 

print('Bem vindo ao Jogo Da Velha do ultimo grupo')
nome = str(input("Qual o seu nome? "))
while True:
    tabul = [' '] * 10
    simboloVoce, simboloComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print ("\n")
    print ("\nPosições jogáveis")
    print ("\n 00 | 01 | 02 ")
    print ("---+---+---")
    print (" 10 | 11 | 12 ")
    print ("---+---+---") 
    print (" 20 | 21 | 22 ")
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
                print("Vencedor: %s" %(nome))
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
