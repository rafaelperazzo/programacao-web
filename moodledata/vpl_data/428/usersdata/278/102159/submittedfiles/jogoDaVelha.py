# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
m=[
    [' ',' ', ' '],
    [' ',' ', ' '],
    [' ',' ', ' ']
]
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=="X":
    X="humano"
    O="computador"
sorteio = sorteio ()
mostraTabuleiro (m)
i=sorteio_i ()
j=sorteio_j ()
jogadaComputador (s,sorteio_i,sorteio_j)
mostraTabuleiro (m)
            