# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=='X':
    X='humano'
    O='computador'
sorteio = sorteio ()
i=sorteio_i ()
j=sorteio_j ()
if s=='X':
    m=jogadaComputador (sorteio_i,sorteio_j)
mostraTabuleiro (m)
            