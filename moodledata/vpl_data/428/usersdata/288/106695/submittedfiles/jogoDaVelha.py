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
    print ("\n 0 0 | 0 1 | 0 2 ")
    print ("-----+-----+---")
    print (" 1 0 | 1 1 | 1 2 ")
    print ("-----+-----+----") 
    print (" 2 0 | 2 1 | 2 2 ")
    print ("\n")  
    print ("______________________________________________")
    print ("\n Começou!")
    if turn=="Voce":
        print("\nVencedor do sorteio para início do jogo:"+nome+" ")
    else:
        print("\nVencedor do sorteio para início do jogo: computador ")
    print ("\n")
    rodando = True

    while rodando:
        if turn == "Voce":
            desenhaTabuleiro(tab)
            movimento = jogadaHumana(tab)
            jogada(tab, simboloVoce, movimento)

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
            jogada(tab, simboloComputador, movimento)

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
print ("\nObrigado por jogar, "+nome+". Até mais!")
