# -*- coding: utf-8 -*-

nome_do_jogador = input("Digite o seu nome: ")

simb = input("Digite um simbolo para jogar: ")
print(simb)
while(True):
    if simb != "X" or simb!= "O" :
        input("Digite um simbolo válido: ")
    else:
        break

print("Seu simbolo foi aceito")