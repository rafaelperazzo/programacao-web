# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
import random 

print('Bem vindo ao Jogo Da Velha do ultimo grupo')
nome = str(input("Qual o seu nome? "))
while True:
    tab = [' '] * 10
    simboloVoce, simboloComputador = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print ("\n")
    print ("\nPosições jogáveis")
    print ("\n 00 | 01 | 02 ")
    print ("----+----+---")
    print (" 10 | 11 | 12 ")
    print ("----+----+----") 
    print (" 20 | 21 | 22 ")
    print ("\n")  
    print ("______________________________________________")
    print ("\n Começou!")
    print("\nVencedor do sorteio para início do jogo: {}".format(turn))
    print ("\n")
    rodando = True

    while rodando:
        if turn == 'Voce':
            desenhaTabuleiro(tab)
            movimento = jogadaHumana(tab)
            movimentacao(tab, simboloVoce, movimento)

            if verificaVencedor(tab, simboloVoce):
                desenhaTabuleiro(tab)
                print("Vencedor: "+nome+"")
                rodando = False
            else:
                if completo(tab):
                    desenhaTabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turn = "Computador"

        else:
            movimento = jogadaComputador(tab, simboloComputador)
            movimentacao(tab, simboloComputador, movimento)

            if verificaVencedor(tab, simboloComputador):
                desenhaTabuleiro(tab)
                print("Vencedor: Computador")
                rodando = False
            else:
                if completo(tab):
                    desenhaTabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turn = "Voce"

    if jogarNovamente():
        continue
    else:
        break
print ("\nObrigado por jogar, "+nome+". Ate mais!")
