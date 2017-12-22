# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao Jogo Da Velha do ultimo grupo')

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
