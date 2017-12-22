# -*- coding: utf-8 -*-

#simbolo = input("Digite o simbolo com o qual deseja jogar [X ou O]: ")
def escolha_de_simbolo():
    while(True) : 
        simbolo = input("Digte o simolo que você deseja jogar [X OU O]: ")   
        if simbolo != X or simbolo != O :
            input("Digite um simbolo válido [X OU O]: ")
        else:
            break