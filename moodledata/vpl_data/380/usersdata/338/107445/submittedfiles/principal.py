# -*- coding: utf-8 -*-

nome_do_jogador = input("Digite o seu nome: ")
X = 1
O = 2

simb = input("Digite um simbolo para jogar: ")

while(True):
    if simb != X or simb!= O :
        input("Digite um simbolo válido: ")
    else:
        break

print("Seu simbolo foi aceito")