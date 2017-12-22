# -*- coding: utf-8 -*-

nome_do_jogador = input("Digite o seu nome: ")
X =1
O = 2

while(True):
    simbolo_do_jogador = str(input("Digite o simbolo com o qual você deseja jogar [X ou O] : "))
    if simbolo_do_jogador != X  or  simbolo_do_jogador != O :
        simbolo_do_jogador = input("Digite um simbolo válido: ")   
    else:
        break
