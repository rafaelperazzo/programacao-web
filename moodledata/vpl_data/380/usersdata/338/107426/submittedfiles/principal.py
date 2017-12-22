# -*- coding: utf-8 -*-

nome_do_jogador = input("Digite o seu nome: ")
simbolo_do_jogador = input("Digite o simbolo com o qual você deseja jogar [1 ou 2] : ")

while(True):
    if simbolo_do_jogador != 1 or  simbolo_do_jogador != 2 :
        simbolo_do_jogador = input("Digite um sibolo válido para voce jogar: ")   
    else:
        break
