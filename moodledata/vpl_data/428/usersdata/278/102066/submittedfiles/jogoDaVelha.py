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
jogadaComputador ()
if s=="X":
    m1=[
        [' ',' ', ' '],
        [' ',' ', ' '],
        [' ',' ', ' ']
    ]
    for i in range (0,3,1):
        for j in range (0,3,1):
            if m1[i][j]==sorteio:
                m1[i][j]=+'O'
                break
    mostraTabuleiro (m1)
            