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
sorteio_i ()
sorteio_j ()
x = jogadaComputador (sorteio_i,sorteio_j)
if s=="X":
    x='O'
    mostraTabuleiro (m)
            