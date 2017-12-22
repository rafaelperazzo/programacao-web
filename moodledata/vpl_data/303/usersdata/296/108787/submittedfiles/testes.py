# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
from jogoDaVelha_BIB import *

print('Bem vindo ao Jogo Da Velha do ultimo grupo')
nome = str(input("Qual o seu nome? "))

while True:
    tab = [' '] * 10
    simbolo_jogador, simbolo_computador = solicitar_simbolos()
    turno_atual = sortear_primeiro_turno()
    print("\n\nPosições jogáveis")
    print("\n 0 0 | 0 1 | 0 2 ")
    print("-----+-----+----")
    print(" 1 0 | 1 1 | 1 2 ")
    print("-----+-----+----")
    print(" 2 0 | 2 1 | 2 2 ")
    print("\n______________________________________________")
    print("\n Começou!")
    if turno_atual == TURNO_JOGADOR:
        print("\nVencedor do sorteio para início do jogo: %s " % nome)
    else:
        print("\nVencedor do sorteio para início do jogo: computador ")
    print("\n")
    i = 0

    while i < 1:
        if turno_atual == TURNO_JOGADOR:
            desenhar_tabuleiro(tab)
            movimento = movimentacao_jogador(tab)
            jogada(tab, simbolo_jogador, movimento)

            if verificar_vencedor(tab, simbolo_jogador):
                desenhar_tabuleiro(tab)
                print("Vencedor: %s" % nome)
                i += 1
            else:
                if tabuleiro_completo(tab):
                    desenhar_tabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turno_atual = TURNO_COMPUTADOR

        else:
            movimento = efetuar_jogada_computador(tab, simbolo_computador)
            jogada(tab, simbolo_computador, movimento)

            if verificar_vencedor(tab, simbolo_computador):
                desenhar_tabuleiro(tab)
                print("Vencedor: Computador")
                i += 1
            else:
                if tabuleiro_completo(tab):
                    desenhar_tabuleiro(tab)
                    print("Deu Velha!")
                    break
                else:
                    turno_atual = TURNO_JOGADOR

    if jogar_novamente():
        continue
    else:
        break
print("\nObrigado por jogar, %s .Até mais!" % nome)


