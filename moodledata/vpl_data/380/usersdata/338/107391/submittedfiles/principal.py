# -*- coding: utf-8 -*-

#simbolo = input("Digite o simbolo com o qual deseja jogar [X ou O]: ")
def escolha_de_simbolo(simbolo):
    while(True) : 
        if simbolo != X or simbolo != O :
            input("Digite um simbolo válido [X OU o]: ")
        else:
            break
    return simbolo 